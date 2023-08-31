size = int(input("Enter the size of the 'A' letter pattern: "))

for i in range(size):
    for j in range(size-i):
        print(" ", end="")
    for j in range(i+1):
        if j == 0 or j == i or i == size//2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
  
