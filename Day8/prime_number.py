def prime_checker(number):
    if number == 1:
        print("Not prime")
    for i in range(2, number):
        if (number % i == 0):
            print("Not prime")
            break
        else:
            print("Prime")
            break


test_number = int(input('Check prime of a number'))
prime_checker(test_number)
