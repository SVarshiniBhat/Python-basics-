### finds given year is leap year or not
year=int(input("Enter year: "))
if (year%4)==0:
    if (year%100)==0:
        if(year%400)==0:
            print("Its Leap Year")
        else:
            print("Its Non-Leap Year")
    else:
        print("Its Leap Year")
else:
    print("Its Non-Leap Year")
