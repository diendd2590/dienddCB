# Bài code học python đầu tiên dùng để encode hoặc decode BASE64 đơn giản thực ra có thể dùng hàm nma tôi viết hàm chủ yếu để hiểu :))
import base64
def endcode64(xau64: bytes) -> str:
    B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    chuoi = ""
    final = ""
    bang = 0  # Khởi tạo mặc định số dấu = bằng 0
    
    for b in xau64: 
        xau8 = f"{b:08b}" # biến một kí tự thành 1 byte 8 bits
        chuoi += xau8
        
    for i in range(0, len(chuoi), 6):
        nhom = chuoi[i : i + 6] # chia các bytes từ 8 -> 6 bits
        if len(nhom) == 6:
            bina = int(nhom, 2) # python mạnh vcl :v
            final += B64[bina]
        else:
            thieu = 6 - len(nhom)
            nhomdu = nhom + ("0" * thieu)
            index = int(nhomdu, 2)
            final += B64[index]
            if thieu == 2:
                bang = 1
            elif thieu == 4:
                bang = 2  # Sửa == thành =
                
    final = final + ("=" * bang) 
    return final

#Chương chương trình chính
print("Bạn muốn ENCODE(E) hay DECODE(D)")
s = input("Lựa chọn: ")

if s == 'E':
    xau64 = input("Nhập xâu kí tự cầnE encode: ").encode('utf-8')
    encoded = endcode64(xau64)
    print("Kết quả :",encoded)
elif s == 'D':
    xau64 = input("Nhập xâu kí tự cần decode: ").encode('utf-8')
    decoded = base64.b64decode(xau64).decode("utf-8")
    print("Kết quả : ",decoded)
else: 
    print("mày có ngu k ??")