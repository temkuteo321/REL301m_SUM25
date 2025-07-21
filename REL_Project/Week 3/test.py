# Import các thư viện cần thiết
from transformers import AutoTokenizer
from trl import PPOTrainer, PPOConfig, AutoModelForCausalLMWithValueHead
from datasets import load_dataset
from difflib import SequenceMatcher
import torch
import os

# ======== Load mô hình đã được fine-tune (SFT) và tokenizer ========
sft_model_path = "C:/Users/84914/Documents/REL_Project/Week 3/sft_model"

# Load tokenizer từ thư mục mô hình đã SFT
tokenizer = AutoTokenizer.from_pretrained(sft_model_path)
# Thiết lập token pad giống token kết thúc nếu chưa được định nghĩa
tokenizer.pad_token = tokenizer.eos_token

# Load mô hình chính để huấn luyện PPO (có thêm head giá trị để PPO sử dụng)
model = AutoModelForCausalLMWithValueHead.from_pretrained(sft_model_path)
# Load mô hình tham chiếu (không cập nhật tham số, dùng để tính KL divergence)
ref_model = AutoModelForCausalLMWithValueHead.from_pretrained("gpt2")

# ======== Load dữ liệu PPO từ file JSON ========
dataset = load_dataset("json", data_files="C:/Users/84914/Documents/REL_Project/Week 3/sft_data_100.json")["train"]

# ======== Hàm đánh giá reward cho mỗi cặp prompt-response ========
def reward_fn(query, response, reference):
    response = response.lower().strip()
    reference = reference.lower().strip()
    query = query.lower().strip()

    # Nếu model trả về đúng câu trả lời thì cho điểm thưởng cao nhất
    if reference == response:
        return 3.0
    elif reference in response:
        return 2.5

    # Nếu câu trả lời lặp lại prompt (dấu hiệu lặp vô nghĩa) thì phạt nặng
    if query in response:
        return 0.1

    # Tính độ tương đồng (fuzzy matching) giữa response và reference
    ratio = SequenceMatcher(None, response, reference).ratio()
    if ratio > 0.9:
        return 2.0
    elif ratio > 0.7:
        return 1.0
    elif ratio > 0.5:
        return 0.5
    return 0.0

# ======== Cấu hình PPO ========
config = PPOConfig(
    model_name=sft_model_path,          # Tên mô hình chính
    learning_rate=5e-6,                 # Learning rate
    batch_size=1,                       # Batch size tổng (số query xử lý mỗi lần)
    mini_batch_size=1,                  # Kích thước mini batch (cho gradient update)
    gradient_accumulation_steps=1,      # Tích lũy gradient (nếu muốn hiệu quả GPU)
    ppo_epochs=4,                       # Số epoch PPO cho mỗi bước dữ liệu
    init_kl_coef=0.05,                  # KL coefficient ban đầu
    target_kl=3.0,                      # KL target để điều chỉnh KL penalty
    log_with=None                       # Không log với wandb/huggingface
)

# ======== Khởi tạo PPOTrainer với model, ref_model và tokenizer ========
trainer = PPOTrainer(
    config=config,
    model=model,
    ref_model=ref_model,
    tokenizer=tokenizer
)

# ======== Tạo thư mục để lưu kết quả huấn luyện ========
os.makedirs("C:/Users/84914/Documents/REL_Project/Week 3/ppo_outputs", exist_ok=True)
os.makedirs("C:/Users/84914/Documents/REL_Project/Week 3/ppo_model", exist_ok=True)

# ======== Vòng huấn luyện PPO ========
best_reward = float("-inf")  # Lưu reward tốt nhất để chọn model tốt nhất

for epoch in range(3):  # Lặp qua 3 epoch PPO
    print(f"\n Epoch {epoch + 1}/3")
    rewards_this_epoch = []  # Danh sách reward để tính trung bình mỗi epoch

    for i, sample in enumerate(dataset):  # Duyệt qua từng mẫu dữ liệu trong tập
        query = sample["prompt"]
        reference = sample["completion"]

        # Tokenize query (prompt) thành input_ids
        input_ids = tokenizer(query, return_tensors="pt", padding=True, truncation=True).input_ids

        # Sinh response từ model
        response_ids = model.generate(
            input_ids=input_ids,
            max_new_tokens=30,             # Số tokens tối đa sinh ra
            do_sample=True,                # Dùng sampling (không greedy)
            top_k=30,
            top_p=0.85,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

        # Decode response ra text
        response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)

        # Tính reward cho cặp prompt-response
        reward = reward_fn(query, response_text, reference)
        rewards_this_epoch.append(reward)

        # PPO Step: Huấn luyện model với query, response và reward
        try:
            trainer.step(
                queries=[input_ids.squeeze(0)],           # Loại bỏ batch dim (batch_size=1)
                responses=[response_ids.squeeze(0)],
                scores=[torch.tensor(reward)]             # reward chuyển thành tensor
            )
        except Exception as e:
            print(f" Skipping step {i} due to error: {e}")
            continue  # Nếu lỗi thì skip bước này

        # Ghi log từng bước ra file
        with open("C:/Users/84914/Documents/REL_Project/Week 3/ppo_outputs/log.txt", "a", encoding="utf-8") as f:
            f.write(f"[Epoch {epoch+1}] Query: {query}\nReference: {reference}\nResponse: {response_text}\nReward: {reward:.2f}\n\n")

        print(f" Step {i+1}/{len(dataset)} | Reward: {reward:.2f}")

    # Sau mỗi epoch, tính reward trung bình
    avg_reward = sum(rewards_this_epoch) / len(rewards_this_epoch)
    print(f" Epoch {epoch+1} DONE - Avg Reward: {avg_reward:.4f}")

    # Nếu reward tốt hơn trước đó thì lưu lại mô hình
    if avg_reward > best_reward:
        best_reward = avg_reward
        model.save_pretrained("C:/Users/84914/Documents/REL_Project/Week 3/ppo_model")
        tokenizer.save_pretrained("C:/Users/84914/Documents/REL_Project/Week 3/ppo_model")
        print("  Saved best model so far!")

print(" PPO training complete.")
