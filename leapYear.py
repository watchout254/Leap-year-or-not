print("\t\t\tWelcome to Changamoto check leap year")
mwaka = int(input("Enter your choice of year you want to check:  "))

if mwaka % 4 == 0:
    if mwaka % 100 == 0:
        if mwaka % 400 == 0:
            print("is a leap year")
        else:
            print("Not a leap year")
    else:
        print(" is a Leap year")
else:
    print("Not a leap year")

print("Thank you!Run the program for clarity.")