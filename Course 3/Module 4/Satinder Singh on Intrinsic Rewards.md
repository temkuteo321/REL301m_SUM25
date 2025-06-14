# Tại sao cần intrisic rewards:
- Trong môi trường RL thực tế, reward bên ngoài (extrinsic reward) thường rất hiếm hoặc chậm – ví dụ khi chỉ được thưởng lớn khi thực hiện đúng nhiệm vụ. Nếu chỉ dựa vào đó, agent khó hoặc không thể học hiệu quả.
- Intrinsic rewards (khen thưởng nội sinh) giúp agent khám phá môi trường, học các kỹ năng nền tảng, như “sự tò mò” và khám phá – cũng như trẻ em chơi để học hành động có ý nghĩa sau này.
# Gốc rễ theo góc nhìn tiến hóa:
- Singh và cộng sự đưa ra một mô hình reward tối ưu (optimal rewards framework): một hàm reward tốt phải giúp agent tối đa hóa fitness (khả năng sinh tồn) qua nhiều môi trường
- Hàm reward tốt không chỉ tiêu chí extrinsic mà còn khuyến khích agent khám phá, chơi đùa, học các kỹ năng nền tảng—những điều quan trọng cho thành công lâu dài.
# Ví dụ mô phỏng:
- Trong bài giảng, Singh trình bày các thí nghiệm “playroom” và “boxes”: agent học mở hộp và khám phá, nhờ intrinsic reward, chuẩn bị cho việc đạt reward extrinsic sau đó.
- Hành vi khám phá (vận động, tương tác) phát triển tự nhiên trước khi có phần thưởng ngoài.
# Phân biệt Intrisic vs Extrinsic:
- Extrinsic reward: khen thưởng trực tiếp giúp đạt mục tiêu (ví dụ ăn, tiêu thụ năng lượng).
- Intrinsic reward: khuyến khích khám phá – giúp agent chuẩn bị sẵn sàng khi cơ hội thực sự xuất hiện. Dịch trong RL, nó trở thành primary reward nội tại, được học, chứ không phải chỉ là tín hiệu bên ngoài.
# Kết luận:
- Intrinsic rewards giúp agent tự học kỹ năng chung, nâng cao khả năng thích nghi.
- Là thành phần quan trọng trong các kỹ thuật RL tiên tiến: curiosity-driven RL (RND, ICM), pseudo-counts, NoisyNet… khi kết hợp với function approximation hoặc deep learning.
- Có thể gắn vào policy gradient hoặc SARSA/DQN để thúc đẩy khám phá
