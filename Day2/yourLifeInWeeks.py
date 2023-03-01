age = int(input("What is your current age?"))
# Assuming life span of 90 years
lifespan = 90
years_left = lifespan - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
message = f"Assuming lifespan of 90 years you have Years:{years_left} Months:{months_left} Weeks:{weeks_left} Days:{days_left}"
print(message)
