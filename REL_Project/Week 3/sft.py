# ============================
# 1. Import thư viện cần thiết
# ============================
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling
)
from datasets import load_dataset


# ==================================
# 2. Load & định dạng lại dữ liệu SFT
# ==================================
# Đường dẫn đến file JSON chứa dữ liệu huấn luyện
data_path = "C:/Users/84914/Documents/REL_Project/Week 3/sft_data_100.json"

# Load tập train từ file JSON
dataset = load_dataset("json", data_files={"train": data_path})["train"]

# Định dạng mỗi dòng thành văn bản dạng "Question: ... Answer: ..."
def format(sample):
    return {"text": f"Question: {sample['prompt']}\nAnswer: {sample['completion']}"}

# Gán format cho toàn bộ dataset
dataset = dataset.map(format)


# ========================================
# 3. Load tokenizer và xử lý pad_token cho GPT-2
# ========================================
model_name = "gpt2"  # hoặc "gpt2-medium", "gpt2-large" nếu bạn có GPU mạnh

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # GPT-2 không có pad_token mặc định

# Tokenize từng sample
def tokenize(sample):
    return tokenizer(sample["text"], padding="max_length", truncation=True, max_length=128)

dataset = dataset.map(tokenize, batched=True)
dataset.set_format(type="torch", columns=["input_ids", "attention_mask"])


# ==============================
# 4. Load mô hình GPT-2 cần huấn luyện
# ==============================
model = AutoModelForCausalLM.from_pretrained(model_name)
model.resize_token_embeddings(len(tokenizer))  # cập nhật nếu tokenizer thay đổi


# ============================
# 5. Cấu hình quá trình huấn luyện
# ============================
training_args = TrainingArguments(
    output_dir="C:/Users/84914/Documents/REL_Project/Week 3/sft_model_new",  # Thư mục lưu checkpoint
    per_device_train_batch_size=2,   # Cần chỉnh nếu bạn có GPU yếu/mạnh
    num_train_epochs=3,              # Huấn luyện trong 3 epoch
    logging_steps=5,
    save_steps=1000,
    save_total_limit=1,              # Chỉ giữ lại checkpoint mới nhất
    learning_rate=5e-5,
    weight_decay=0.01,
    fp16=False,                      # Bật True nếu dùng GPU có hỗ trợ
    report_to="none"                 # Không dùng wandb hay tensorboard
)

# Data collator: gom các sample lại thành batch mà không mask (vì GPT-2 không dùng MLM)
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # GPT-2 là mô hình sinh, không dùng masked language modeling
)


# ============================
# 6. Huấn luyện mô hình
# ============================
trainer = Trainer(
    model=model,
    tokenizer=tokenizer,
    args=training_args,
    train_dataset=dataset,
    data_collator=data_collator
)

# Bắt đầu huấn luyện
trainer.train()


# ============================
# 7. Lưu mô hình và tokenizer đã fine-tune
# ============================
save_path = "C:/Users/84914/Documents/REL_Project/Week 3/sft_model"
trainer.save_model(save_path)
tokenizer.save_pretrained(save_path)
