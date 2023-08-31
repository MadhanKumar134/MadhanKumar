pwd=int(input("Enter the password :"))
if pwd==123:
    pwd=int(input("Enter the Password :"))
    if pwd==456:
        pwd=int(input("Enter the password :"))
        if pwd==789:
            print("Valid User")
        else:
            print("1st and 2nd is right but 3rd is incorrect")
    else:
        print("1st is right but 2nd is wrong")
else:
    print("Invalid credentials")
