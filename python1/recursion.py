def fact(n):
    if n==1 or n==0:
        return 1
    factorial = n*fact(n-1)
    return factorial

f=fact(8)
print(f)