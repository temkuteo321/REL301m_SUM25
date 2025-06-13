# Mục tiêu của Gradient Descent trong Neural Networks:
![image](https://github.com/user-attachments/assets/d217b5a8-104f-4430-89c2-5ccf26f831e8)
# Forward – Backprop – Update Loop:
![image](https://github.com/user-attachments/assets/af32c0eb-618d-4f19-ac7b-01a6178cab70)
# Chiến lược cập nhật nâng cao:
- Mini-batch GD: chọn một nhóm nhỏ mẫu để tính gradient → ổn định hơn SGD và hiệu quả hơn batch GD
- Adaptive optimizers: như Adam, RMSProp giúp tự điều chỉnh learning rate cho từng tham số, thường được dùng trong Deep Learning .
# Tối ưu để ổn định và tránh overfitting:
- Learning rate schedule: giảm dần 
𝛼
α theo epochs để tăng độ ổn định cuối cùng
- Early stopping: dừng training khi hiệu năng trên tập validation không cải thiện nữa – giúp tránh overfit
- Regularization (Dropout, L2…), normalization (BatchNorm) cũng thường được áp dụng
# Thách thức trong môi trường RL:
- Trong RL, dữ liệu không i.i.d, target thường phụ thuộc mạng (bootstrap), nên dễ gây không ổn định khi training.
- Cần dùng thêm các kỹ thuật như Experience Replay, Target Networks, gradient clipping, và điều chỉnh kiến trúc cũng như hyperparameters cẩn thận .


