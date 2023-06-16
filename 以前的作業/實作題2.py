import random
def x():#乘   
    right=wrong=0 
    while True:
        a=int(random.randint(1,99))
        b=int(random.randint(1,99))
        answer=int(input("請問{}x{}等於多少? ".format(a,b)))
        if answer==a*b:
            print("答對了")
            right+=1
        else:
            print("答錯了，正確答案是:",a+b)
            wrong+=1
        q=input("請問還要繼續練習嗎(y/n)?")
        if q !='y'and q != 'Y':
            break
    print("你總共答對{}題，答錯了{}題。".format(right,wrong))
def x2():#+
    right=wrong=0
    while True:
        a=int(random.randint(1,99))
        b=int(random.randint(1,99))
        answer=int(input("請問{}+{}等於多少? ".format(a,b)))
        if answer==a+b:
            print("答對了")
            right+=1
        else:
            print("答錯了，正確答案是:",a+b)
            wrong+=1
        q=input("請問還要繼續練習嗎(y/n)?")
        if q !='y'and q != 'Y':
            break
    print("你總共答對{}題，答錯了{}題。".format(right,wrong))
def xx():#-
    right=wrong=0
    while True:
        a=int(random.randint(1,99))
        b=int(random.randint(1,99))
        answer=int(input("請問{}-{}等於多少? ".format(a,b)))
        if answer==a-b:
            print("答對了")
            right+=1
        else:
            print("答錯了，正確答案是:",a+b)
            wrong+=1
        q=input("請問還要繼續練習嗎(y/n)?")
        if q !='y'and q != 'Y':
            break
    print("你總共答對{}題，答錯了{}題。".format(right,wrong))

cc=input("+:1  -:2  *:3")
if cc=="1":
    x2()
elif cc=="2":
    xx()
else:
    x()
#由小冰製作