# Tile coding là gì:
- Đây là một kỹ thuật coarse coding dùng để biểu diễn không gian trạng thái liên tục bằng nhiều lưới (tilings) với các ô (tiles) che phủ toàn bộ không gian, mỗi tile là một đặc trưng nhị phân (on/off
- Khi một trạng thái 
𝑠
s được quan sát, nó sẽ kích hoạt đúng một tile trong mỗi tiling tương ứng với tọa độ của nó, tạo ra tập các feature active.
# Tại sao lại dùng tilings?
![image](https://github.com/user-attachments/assets/76f5b32e-5293-4935-af1a-ca765c540342)
# Tính toán giá trị gần đúng:
![image](https://github.com/user-attachments/assets/23eb5ae0-eddf-4715-b3d6-b3639635a048)
# Ưu-nhược:
- Ưu điểm:
   + Tăng khả năng tổng quát hóa hiệu quả và nhanh với cost tính toán O(number of tilings).
   + Cấu trúc sparse giúp dễ tích hợp vào thuật toán tuyến tính hoặc mạng neura
- Nhược điểm:
   + Cần thiết kế và điều chỉnh số lượng tilings, kích thước mỗi tile, cách dịch offset sao cho phù hợp với bài toán — nếu không, có thể underfit hoặc overfit.
   + Độ phức tạp và kích thước bộ nhớ tăng theo số tilings và độ phức tạp không gian trạng thái


