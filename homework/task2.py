year = int(input("Enter year: "))

if year % 4 != 0:
    print("Is not a Leap Year")
elif year % 100 != 0:
    print("Is a Leap Year")
elif year % 400 == 0:
    print("Is a Leap Year")
else:
    print("Is not a Leap Year")