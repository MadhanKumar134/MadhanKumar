'''i=1
s=1
while i<=10:
    if i==10:
        print(i)
        s*=i
        i+=1
    else:
        print(i,end="*")
        s*=i
        i+=1
print("sum of give numbers:",s)'''



'''i=10
while i>=1:
    print(i)
    i-=1'''


'''i=1
s=0
while i<=10:
    if i==10:
        print(i,end="=")
        i+=1
    elif i%2==0:
        print(i,end="+")
        s-=i
        i+=1
    else:
        print(i,end="-")
        s+=i
        i+=1
print(s)'''



a=int(input("Enter the value:"))
s=0
while a!=0:
    s+=a
    print(a)
    a=int(input("Enter the value:"))
print("The sum of given numbers are :",s)
