bill = float(input("What is the total bill?"))
tip_percentage = int(
    input("What percentage of tip you would like to give?"))/100
people = int(input("How many people are splitting the bill?"))
pay_amount_per_person = (bill+bill*tip_percentage)/people

# print(f"Each person should pay {%.2f}.format{}")
print("{:.2f}".format(pay_amount_per_person))
