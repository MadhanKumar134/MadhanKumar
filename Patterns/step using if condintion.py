for i in range (1,6):
    for j in range (1,6):
        if i<=j:
            print(i,j,end=" ")
        else:
            print("   ", end=" ")
    print()
