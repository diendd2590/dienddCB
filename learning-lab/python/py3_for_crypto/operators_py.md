## Đầu tiên thì chúng ta sẽ nói sơ qua về một số toán tử đặc biệt là bitwise
| Toán tử | Tên gọi | Tác dụng bitwise | Bản chất toán học / Ứng dụng | Ví dụ ($x = 5$, $y = 3$) | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `&` | **AND** | Giữ lại bit $1$ nếu cả 2 cùng là $1$, gặp $0$ là ép về $0$. | **Bitmask** (Lọc lấy các bit cần thiết, xóa bit thừa). | `5 & 3` (`0101 & 0011`) | `1` (`0001`) |
| `\|` | **OR** | Chỉ cần 1 trong 2 là $1$ thì kết quả là $1$. | Phép gộp bit (ghép các byte lại thành 1 khối số lớn). | `5 \| 3` (`0101 \| 0011`) | `7` (`0111`) |
| `^` | **XOR** | Hai bit khác nhau ra $1$, giống nhau ra $0$. | Phép cộng không nhớ (mã hóa đối xứng, đố vui crypto). | `5 ^ 3` (`0101 ^ 0011`) | `6` (`0110`) |
| `~` | **NOT** | Đảo ngược bit ($0 \rightarrow 1, 1 \rightarrow 0$). | Công thức bù 2: **$-(x + 1)$**. | `~5` | `-6` |
| `<<` | **Left Shift** | Dịch bit sang trái $n$ vị trí (thêm $0$ vào đuôi). | **Phép nhân $x \times 2^n$**. | `5 << 2` (`0101 << 2`) | `20` (`10100`) |
| `>>` | **Right Shift** | Dịch bit sang phải $n$ vị trí (vứt bỏ $n$ bit cuối). | **Phép chia lấy nguyên $\lfloor x / 2^n \rfloor$**. | `19 >> 2` (`10011 >> 2`) | `4` (`00100`) |

**Ngoài cái bảng ở trên thì mình cũng sẽ nói sơ về ví dụ thực tế mình hiểu và sẽ cập nhập thêm ns có thứ thú vị (vì đây là lần đầu mình cố hiểu nó :))**

1. Là áp dụng '<<' và '>>' trong python cú pháp của nó sẽ là 'a << n' và 'a >> n' biểu thị cho dịch các bits sang bên trái hoặc bên phải n bước và đồng nghĩa với a * 2 ^ n và  int(a / 2 ^ n) chia nguyên thì thay vì dùng cộng trừ nhân chia thì cái này chạy nhanh hơn nhiều
2. Là áp dụng '&' hay AND ta hiểu cách ns so sánh và hoạt động các bit như bảng trên có thể lấy ví dụ thao tác khi đổi từ dec sang base64: thì ta hiểu mỗi chữ cái t nhập vào đều có giá trị là 1 bytes vs trg hợp có dấu như tiếng việt như 'ô' thì ns là 2 bytes emoji là 3 - 4 bytes , 1 bytes = 8 bits thì base64 đơn giản là tách ns ra thành nhóm 6 bit thay vì 8 và đổi vs bảng đối chiếu base 64

```text
Phần đằng trước (A & B)     |  6 bit khối C
  ?  ?  ?  ?  ?  ?  ?  ?  ? |  1  0  1  1  0  1   (Dãy bit nguyên bản của C)
& 0  0  0  0  0  0  0  0  0 |  1  1  1  1  1  1   (Số 63 dạng nhị phân)
-------------------------------------------------
  0  0  0  0  0  0  0  0  0 |  1  0  1  1  0  1   (KẾT QUẢ)
  |_______________________|   |_______________|
      Gặp 0 -> Xóa sạch          Gặp 1 -> GIỮ NGUYÊN 101101!

Thay vì thao tác bằng xâu thì chúng ta có thể làm ntn dùng dịch phải >> 18 bits đổi vs nhóm 24 thì nhóm 6 cuối là nhóm mình cần lấy rồi lại đem nhóm đó '&' với 63(00111111) các byte còn thiếu trc sẽ tự động được bù bằng các số 0
0 & 0 hay 1 & 0 thì vẫn = 0 thì chúng ta triệt tiêu dc đằng trc còn 111111 đảm báo ta có 6 bít sau hoàn vẹn để lấy ra encode

