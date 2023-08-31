unit=int(input("Enter a unit:"))
fixedcharge=25

if(unit>0 and unit<101):
    print("bill amount:",fixedcharge)
elif(unit>100 and unit<201):
    total=((unit-100)*2)+fixedcharge
    print("bill amount:",total)
elif(unit>200 and unit<301):
    total=((200-100)*2)+((unit-200)*3)+fixedcharge
    print("bill amount:",total)
elif(unit>300 and unit<501):
    total=((200-100)*2)+((300-200)*3)+((unit-300)*5)+fixedcharge
    print("bill amount:",total)
elif(unit>500):
    print("Contact EB office due to excess unit")
else:
    print("No charge due to no unit")

