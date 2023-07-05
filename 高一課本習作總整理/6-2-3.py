data = "76 98 42 90 80 62"
data = data.split()
scores = list()
for item in data:
    scores.append(int(item))
print(scores)
print(" 總分是：", sum(scores))
print(" 最高分：", max(scores))
print(" 最低分：", min(scores))
print("平均是:", sum/len(data))
print(sorted(data,reverse=True))