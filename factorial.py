def factorial (n):
    if n>0:
        a=n*factorial(n-1)
    return (a)
a=int(input ("ingese el número"))
print(factorial(a))