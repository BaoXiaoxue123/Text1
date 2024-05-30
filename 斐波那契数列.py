def fbnqsl(n):
    if n == 1 or n == 2:
        return 1
    return fbnqsl(n-1)+fbnqsl(n-2)


print(fbnqsl(5))