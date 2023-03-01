size = input(print("What size of pizza do you want? (small,medium,large)\n"))
extra_pepperoni = input(print("Extra pepperoni?(yes,no)\n"))
extra_cheese = input(print("Extra cheese?(yes,no)\n"))

small_pizza = 15
medium_pizza = 20
large_pizza = 25

small_pepperoni_price = 2
medium_and_large_pepperoni_price = 3

extra_cheese_price = 1

final_bill = 0
if size == "small":
    final_bill += small_pizza
if size == "medium":
    final_bill += medium_pizza
if size == "large":
    final_bill += large_pizza
if extra_pepperoni == 'yes':
    if size == "large":
        final_bill += medium_and_large_pepperoni_price
    else:
        final_bill += small_pepperoni_price
if extra_cheese == "yes":
    final_bill += extra_cheese_price

print(f'Your final bill{final_bill}')
