# Import các thư viện cần thiết
from transformers import AutoTokenizer                       # Dùng để load tokenizer tương ứng với mô hình
from trl import PPOTrainer, PPOConfig, AutoModelForCausalLMWithValueHead  # Các thành phần chính của TRL
from datasets import load_dataset                            # Dùng để load dữ liệu
import torch                                                 # Thư viện tính toán tensor
import os                                                    # Thư viện thao tác hệ thống (tạo thư mục, ...)

# 1. Khai báo tên mô hình gốc
model_name = "gpt2"

# 2. Load tokenizer tương ứng với mô hình
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # Thiết lập token dùng để padding là EOS token

# 3. Load tập dữ liệu từ file JSON (được chia thành tập "train")
dataset = load_dataset("json", data_files="C:\\Users\\84914\\Documents\\REL_Project\\Week 2\\trl_textgeneration\\datas\\train.json")["train"]

# 4. Load mô hình GPT-2 có thêm ValueHead (dùng trong PPO để tính giá trị)
model = AutoModelForCausalLMWithValueHead.from_pretrained(model_name)
ref_model = AutoModelForCausalLMWithValueHead.from_pretrained(model_name)  # Mô hình tham chiếu, không cập nhật

# 5. Cấu hình PPO: tên mô hình, learning rate, batch size,...
config = PPOConfig(
    model_name=model_name,
    learning_rate=1e-5,         # Tốc độ học thấp (cẩn trọng với LLM)
    batch_size=1,               # Batch size nhỏ (vì huấn luyện từng sample)
    log_with=None               # Không sử dụng hệ thống logging như WandB
)

# 6. Khởi tạo PPOTrainer với cấu hình, mô hình, tokenizer và tập dữ liệu
trainer = PPOTrainer(
    config=config,
    model=model,
    ref_model=ref_model,
    tokenizer=tokenizer,
    dataset=dataset
)

# 7. Tạo thư mục outputs để lưu log nếu chưa có
os.makedirs("outputs", exist_ok=True)

# 8. Vòng lặp qua từng sample trong tập dữ liệu
for sample in dataset:
    query = sample["query"]  # Lấy prompt từ sample (đầu vào)

    # Chuyển query thành tensor input cho mô hình
    input_ids = tokenizer(query, return_tensors="pt", padding=True, truncation=True).input_ids

    # Sinh văn bản phản hồi từ mô hình dựa trên input
    response_ids = model.generate(
        input_ids=input_ids,
        max_new_tokens=30,                           # Giới hạn độ dài phản hồi
        pad_token_id=tokenizer.eos_token_id          # Đảm bảo padding đúng cách
    )
    # Giải mã (decode) tensor thành chuỗi văn bản
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)

    # Tạo reward giả lập: mỗi 10 từ được +1 điểm
    reward = len(response_text.split()) / 10.0

    # Chuyển query và response sang dạng tensor đơn lẻ (không batch)
    query_tensor = tokenizer(query, return_tensors="pt", padding=True, truncation=True).input_ids[0]
    response_tensor = response_ids[0]
    reward_tensor = torch.tensor(reward)  # Reward dạng tensor

    # Gọi một bước huấn luyện PPO
    trainer.step([query_tensor], [response_tensor], [reward_tensor])

    # Ghi log kết quả vào file để theo dõi
    with open("outputs/output_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Query: {query}\nResponse: {response_text}\nReward: {reward}\n\n")

    # In kết quả ra console
    print(" Query:", query)
    print(" Response:", response_text)
    print(" Reward:", reward)

# 9. Sau khi huấn luyện xong: tạo thư mục models nếu chưa có
os.makedirs("models", exist_ok=True)

# 10. Lưu mô hình và tokenizer đã tinh chỉnh vào thư mục
model.save_pretrained("models/gpt2-ppo-finetuned")
tokenizer.save_pretrained("models/gpt2-ppo-finetuned")
