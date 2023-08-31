def sod(n):
    if n==0:
        return 0
    else:
        return n%10 + sod(n//10)
n=int(input("Enter the Value :"))
res=sod(n)
print("Sum of digits:",res)

