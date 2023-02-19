import random
import string

password_letters = list(string.ascii_letters)
numbers = list(range(10))
symbols = list({'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%',
                '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'})
combined_list = password_letters + numbers + symbols

# password_length = input("Provide password length")
password_length_letters = input("Provide password letter length")
password_length_numbers = input("Provide password number length")
password_length_symbols = input("Provide password symbol length")
password = []


for i in range(int(password_length_letters)):
    # password += str(combined_list[random.randint(0, len(combined_list)-1)])
    password += str(random.choice(password_letters))

for i in range(int(password_length_numbers)):
    # password += str(combined_list[random.randint(0, len(combined_list)-1)])
    password += str(random.choice(numbers))

for i in range(int(password_length_symbols)):
    # password += str(combined_list[random.randint(0, len(combined_list)-1)])
    password += str(random.choice(symbols))


print(password, "".join(random.sample(password, len(password))))
