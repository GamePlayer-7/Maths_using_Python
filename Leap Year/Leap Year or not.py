year = int(input("Enter Year: "))   #User enters the year
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
