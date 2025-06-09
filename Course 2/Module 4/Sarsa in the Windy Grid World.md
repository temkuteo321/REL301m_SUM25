# 1.Mô tả môi trường Windy Grid World:
- Mô hình lưới (grid) có gió (wind) dịch chuyển agent lên một vài ô mỗi lần di chuyển qua vùng gió.

- Mỗi bước đi cộng -1 điểm; mục tiêu là di chuyển từ vị trí xuất phát đến đích với tổng phạt nhỏ nhất
# 2. Cách hoạt động của thuật toán Sarsa:
- Sử dụng cập nhật TD theo công thức:
  ![image](https://github.com/user-attachments/assets/2c532652-adf8-4c16-96a2-3bbfec072ae1)
-  Đây là phương pháp học on-policy: lựa chọn hành động A theo ε‑greedy từ chính sách đang được học, sau đó quan sát S', chọn A' từ cùng chính sách, rồi cập nhật
-  Quy trình tiếp tục trong mỗi bước và mỗi episode cho đến khi đạt đích.
# 3. Kết quả hành vi agent: 
- Sarsa học cách điều hướng vòng quanh những vùng gió, tránh rẽ ngang vô ích và tận dụng gió hỗ trợ đi nhanh hơn.
- Chính sách học được dẫn đến hành vi “thận trọng” hơn so với Q‑learning – chọn đường an toàn hơn, ít rủi ro hơn
# 4.Ưu điểm của Sarsa trong Wind:
- On-policy & ổn định: vì học theo chính sách thực thi nên Sarsa thích ứng tốt với gió thay đổi .

- Bootstrapping tức thời: cập nhật sau mỗi bước đi giúp agent điều chỉnh nhanh khi gặp vùng gió.

- Mô phỏng thử nghiệm trên Windy Gridworld cho thấy cách học của Sarsa phù hợp để đưa ra hành động hợp lý trong điều kiện không ổn định.
