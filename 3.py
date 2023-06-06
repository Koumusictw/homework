def f(n,m):
    if n>m:
        return 0
    return n+f(n+1,m)
a=int(input())
b=int(input())
print(f(a,b))
#此程式由阿昊提供，小冰改寫
