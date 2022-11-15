year = int(input("Provide a year to check\n"))


def year_checker(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("Leap year")
    else:
        print("Not leap year")


year_checker(year)
