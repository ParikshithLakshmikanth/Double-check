num = int(input("Enter Num: "))

if num>50:
    print("The number is greater than 50",end=" ")
    if num%2==0:
        print("and is even too")
    else:
        print("and is odd too")
else:
    print("The number is less than 50")