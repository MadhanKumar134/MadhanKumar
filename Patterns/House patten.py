for i in range (1,5):
    for j in range (1,8):
        if (1+j==5 or i-j==-3):
            print(i,j,end=" ")
        else:
            print(end="     ")
    print()
for i in range (1,6):
    for j in range(1,6):
        if (i==1 or i==5)or(j==1 or j==5):
            print(" ",i,j,end=" ")
        else:
            print(end="      ")
    print()
