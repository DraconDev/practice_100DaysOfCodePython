def year_checker(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return ("Leap year")
    else:
        return ("Not leap year")


# year_checker(int(input("Provide a year to check\n")))

print(year_checker(int(input("Provide a year to check\n"))))
