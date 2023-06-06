def f(n,m):
    if n>m:
        return 0
    return n+f(n+1,m)
a=int(input())
b=int(input())
print(f(a,b))