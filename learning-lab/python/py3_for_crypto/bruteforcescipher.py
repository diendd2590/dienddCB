def brute_caesar(s):
    for i in range(1, 26):
        res = ""
        for x in s:
            tt = ord(x)
            if x.islower(): 
                res += chr((tt - 97 - i) % 26 + 97)
            elif x.isupper(): 
                res += chr((tt - 65 - i) % 26 + 65)
            else: 
                res += x
        print(f"Test với shift {i:02d}: {res}")

s = input("Nhập vào xâu kí tự cần giải: ")
brute_caesar(s)

#Đây là code brute force mã caesar 26 cách thì mã caesar chỉ hiểu là ns là dịch bao nhiêu đơn vị th
