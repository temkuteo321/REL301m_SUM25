# Mục tiêu sử dụng Tile Coding:
- Kỹ thuật tile coding được áp dụng để biểu diễn không gian trạng thái liên tục thành các feature nhị phân — mỗi trạng thái kích hoạt một tập các tile (một tile trong mỗi tiling).
- Mục đích chính: vừa giữ được khả năng tổng quát hóa, vừa đảm bảo phân biệt trạng thái đủ tốt khi kết hợp với thuật toán semi-gradient TD(0)
# Cách tích hợp với TD(0):
![image](https://github.com/user-attachments/assets/362314fe-0f35-4581-a19a-a2353d63deb9)
# Lí do lựa chọn Tile Coding:
- Feature từ tile coding rất sparse, ngăn chặn catastrophic interference khi học online.
- Nó cung cấp cấu trúc cục bộ: trạng thái gần nhau chia sẻ nhiều tile, giúp lan truyền thông tin hiệu quả qua lưới
- Hỗ trợ ổn định cho cả các mô hình tuyến tính và mạng neural incremental.
# Lợi ích:
![image](https://github.com/user-attachments/assets/67a53874-cc10-4ee5-ab82-50269dddb77d)

