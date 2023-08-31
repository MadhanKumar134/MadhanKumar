a=['Naveen','Madhi','Durai','Karthi']
b=a.copy()
c=a[:]
b[0]='Kalai'
c[1]='Arasan'

print(a)
print(b)
print(c)
sum=0
for i in (a,b,c):
    if i[0]=='Kalai':
        sum+=1
    if i[1]=='arasan':
        sum+=10
print(sum)
