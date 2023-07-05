stu1 = ["王大明", 174, 65]
stu2 = ["林小華", 168, 58]
stu3 = ["許中和", 182, 70]
stu4 = ["趙小慧", 159, 45]

body_info = [stu1, stu2, stu3, stu4]
for info in body_info:
    print(info[0],"bmi",round((info[2]/(info[1]/100)**2),2))