list_tiangan=["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
list_dizhi=["子", "醜", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
list_tiandi=[]

for str in list_tiangan:
    for str2 in list_dizhi:
        list_tiandi.append(str+str2)
print(list_tiandi)