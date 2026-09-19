Ở bài này nó cho mình một cái public key của mã RSA như trong ảnh
<img width="706" height="428" alt="image" src="https://github.com/user-attachments/assets/1ebebab8-a9ca-463b-ba7c-a43c6e968f58" />

Vì là lần đầu tiên tiếp xúc với nó mình sẽ viết lại sơ qua về loại mã hóa này

Đây là một dạng mã hóa bất đối xứng *Asymmetric Encryption* cơ bản là nó sẽ tạo ra 2 cái key là public key và private key
public key sẽ có dạng (e,n) private key có dạng là (d,n)
n là tích của 2 số nguyên tố cùng nhau được chọn (ví dụ là 13 thì cá số dưới nó đều là nt cùng nhau)

Các bước mã hóa nếu có public key
có 2 số p và q là 2 số nt cùng nhau -> n chọn một e là key công thức gửi đi sẽ là c ^ e mod n
liên hệ của public key vs private key là (e * d) mod đảo mol (N) = 1
muốn giải mã ta có công thức c^d mod n với các số bé dưới 400 bits hoàn toàn có thể dùng tool để suy ra p và q từ n nma ng ta th g
dùng kiểu mã hóa này với n tầm 2048 bits nên việc phân tích ra là cực kì khó 

Với bài này ta chỉ đơn giản ném vào dcode/rsa-cipher nhập thông điệp và key public và và nó vẫn đnhs ra được cái cờ là ntn 

*picoCTF{sma11_N_n0_g0od_1dc7ae91}*
