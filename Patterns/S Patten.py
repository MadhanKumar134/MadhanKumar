for i in range (1,6):
    for j in range (1,6):
        if(i==1 or i==5)or(j==1 and i!=4)or(j==5 and i!=2)or i==3:
            print(i,j,end=" ")
        else:
            print("",end="    ")
    print()
