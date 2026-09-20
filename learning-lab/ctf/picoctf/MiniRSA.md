Ở bài này nó cho mình một đoạn mã n rất dài và một thông điệp số rất dài 

<img width="708" height="437" alt="image" src="https://github.com/user-attachments/assets/20704961-c5bb-4e65-b0fe-53e23f9f586a" />
Thì ta thấy số e ở đây rất bé và hint của chính bài nữa

Quay lại công thức rsa ở bài trước thì ta thấy có 2 trường hợp xảy ra nếu e bé

1. Là ns chưa đủ để mod n hoạt động nên phép toán ns bây h chỉ là c ^ e quá đơn giản để back
2. Là mod n với chạy được vài lần thì chỉ cần brute force bằng python là ra như code dưới đây:
