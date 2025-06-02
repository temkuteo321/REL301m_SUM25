# Example 1: Grid World Navigation (Simple Robot)
Scenario: Một rô-bốt điều hướng lưới 3x3 để đạt được mục tiêu trong khi tránh chướng ngại vật. Đây là một ví dụ phổ biến để minh họa cho MDP.

Các trạng thái ($ S $): Mỗi ô trong lưới 3x3 là một trạng thái, được đánh số từ 1 đến 9:

1 | 2 | 3
-----------
4 | 5 | 6
-----------
7 | 8 | 9
Trạng thái 3 là mục tiêu (trạng thái cuối).
Trạng thái 5 là chướng ngại vật (không thể ở lại hoặc đi qua).

Hành động ($ A $): Robot có thể di chuyển lên, xuống, sang trái hoặc sang phải.

Xác suất chuyển tiếp ($ P $): Các chuyển động là xác định trừ khi robot đâm vào tường hoặc chướng ngại vật, trong trường hợp đó robot sẽ ở nguyên vị trí. Ví dụ:

Từ trạng thái 1, "phải" → trạng thái 2.

Từ trạng thái 1, "xuống" → trạng thái 4.

Từ trạng thái 1, "trái" hoặc "lên":

Phần thưởng ($ R $):

$ R = -1 $ cho mỗi lần di chuyển (để khuyến khích đạt được mục tiêu nhanh chóng).
$ R = +10 $ cho việc đạt được mục tiêu (trạng thái 3).
Nếu robot cố gắng vào trạng thái 5 (chướng ngại vật), nó sẽ ở nguyên vị trí và nhận được $ R = -1 $.

Hệ số chiết khấu ($ \gamma $): $ \gamma = 0,9 $ (phần thưởng trong tương lai được chiết khấu).
Mục tiêu: Tìm một chính sách $ \pi $ tối đa hóa phần thưởng tích lũy dự kiến, hướng dẫn robot đến trạng thái 3 trong khi tránh trạng thái 5.

MDP trong hành động: Bắt đầu ở trạng thái 1, robot có thể đi "bên phải" đến trạng thái 2 ($ R = -1 $), sau đó "bên phải" đến trạng thái 3 ($ R = +10 $), kết thúc tập phim. Giá trị của trạng thái 1 theo một chính sách tối ưu sẽ tính đến phần thưởng chiết khấu dọc theo con đường tốt nhất đến mục tiêu.
