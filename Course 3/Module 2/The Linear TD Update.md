# Biểu diễn tuyến tính (Linear Function Approximation):
![image](https://github.com/user-attachments/assets/b14dcb1d-23c3-4f21-9746-b5723de2bd23)
# Update rule cho TD(0) tuyến tính:
![image](https://github.com/user-attachments/assets/80da8221-01d4-4527-80cf-f9bad05e2f37)

Đây là công thức semi-gradient TD(0) với biểu diễn tuyến tính, do gradient của phần bootstrap (với 
𝑠
𝑡
+
1
s 
t+1
​
 ) bị bỏ qua.

# Giải thích và phân tích
![image](https://github.com/user-attachments/assets/3de9e463-1551-4696-a668-1f79eb2c1f59)
# Ưu-nhược:
- Ưu điểm:
   + Tính toán mỗi bước đơn giản, tiết kiệm O(d) thời gian (d = số feature)
   + Hội tụ với điều kiện on-policy và linear
- Nhược điểm:
   + Mục tiêu bootstrap gây bias so với gradient “thật”.
   + Với off-policy, có thể dẫn đến không ổn định/divergence nếu không dùng thuật toán điều chỉnh (như GTD) .
