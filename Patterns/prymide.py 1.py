row = int(input("Enter numbers of row:"))
space = row-1
for i in range (0,row):
    print(end=" ")
    space=space-1
    for k in range (0, i+1):
        print("* ", end="")
    print()
