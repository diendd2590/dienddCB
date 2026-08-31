### 1. Phân biệt Encoding (Base64) và Encryption (Mã hóa bảo mật)

- **Encryption (Mã hóa bảo mật):** Dùng để bảo vệ bí mật dữ liệu (ví dụ: AES, RSA). Muốn giải mã bắt buộc phải có **khóa giải mã (Secret Key)** hoặc mật khẩu.
- **Encoding (Mã hóa biểu diễn):** Dùng để **biến đổi định dạng dữ liệu** giúp truyền tải an toàn qua các giao thức chỉ hỗ trợ văn bản (như Email, HTTP Header), tránh bị lỗi định dạng trên đường truyền.
- **Lưu ý:** Base64 **KHÔNG CÓ tính bảo mật**. Bất kỳ ai cũng có thể giải mã chuỗi Base64 về dữ liệu gốc chỉ trong vài giây mà không cần bất kỳ mật khẩu nào.

---

### 2. Mối quan hệ giữa Base64 và ASCII

- **Base64 KHÔNG PHẢI là bản mở rộng của ASCII.**
- Dữ liệu nhị phân thô (ảnh, nhạc, file `.exe`) chứa nhiều byte rác hoặc ký tự điều khiển ASCII không in được, khiến các hệ thống truyền văn bản dễ bị lỗi.
- Base64 giải quyết vấn đề này bằng cách **mượn 64 ký tự ASCII in được an toàn nhất** (`A-Z`, `a-z`, `0-9`, `+`, `/`) để đại diện cho toàn bộ dữ liệu nhị phân đó.

---

### 3. Cơ chế hoạt động cốt lõi (Từ 8-bit sang 6-bit)

Dù dữ liệu gốc là chữ (ASCII 8-bit), điểm ảnh (RGB 8-bit), hay sóng âm thanh, máy tính đều quy tất cả về các Byte nhị phân 8-bit.

- **Quy trình chuyển đổi:**
  1. Gom nhóm **3 Bytes** dữ liệu gốc ($3 \times 8\text{-bit} = 24\text{ bits}$).
  2. Chia 24 bits đó thành **4 nhóm nhỏ**, mỗi nhóm **6-bit** ($4 \times 6\text{-bit} = 24\text{ bits}$).
  3. Giá trị của nhóm 6-bit ($0 \rightarrow 63$) được tra theo bảng mã Base64 để đổi thành ký tự ASCII tương ứng.
  4. Nếu dữ liệu không đủ bộ 3 Bytes, hệ thống sẽ chèn thêm bit 0 và dùng dấu `=` (Padding) ở cuối để đánh dấu đệm bù.
 
  5. **Kiến thức bổ ích từ những thắc mắc của tôi :))**

  1. **Cái gì phụ trách encode ?** -> Đây là một quá trình khá cơ bản nên hầu như trên các thiết bị thì các phần cứng chịu     trách nghiệm này như trên điện thoại chụp ảnh thì chip đã tự ghi nhị phân trên từng pixel rồi còn các thư viện giúp nữa       còn nhiều thì tôi từ chỗi hiểu :)) | với web thì có các cái tích hợp sẵn trên gg firefox trên java như btoa() atob()

  
