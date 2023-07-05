def x():
    number = int(input("請輸入一個要轉換成二進位的數字；"))
    binary = list()
    while number > 1:
        binary.append(str(number %2))
        number //= 2
    binary.append(str(number))
    print("".join(reversed(binary)))
def x2():
    number = int(input("請輸入一個要轉換成八進位的數字；"))
    binary = list()
    while number > 1:
        binary.append(str(number %8))
        number //= 8
    binary.append(str(number))
    print("".join(reversed(binary)))
def x3():
    decimal=int(input("請輸入一個要轉換成十六進位的數字；"))
    print(hex(decimal))
cc=input("+:1二進位  -:2八進位  *:3十六進位")
if cc=="1":
    x()
elif cc=="2":
    x2()
else:
    x3()