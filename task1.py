# предварительный отбор кандидатов на должность программиста
name = input("Hello! Please, enter your first name")
surname = input("Please, enter your last name")
print(f"The name of candidate for the position of a programmer is {surname} {name}")
age = int(input("Please, enter your age"))
if age < 18:
    print("Oh! Your're so young!")
print(f"The age of candidate for the position of a programmer is {age}")
experience = int(input("How many years have you been programmer?"))
while experience > age:
    print("Ups! Maybe you made a mistake. Your experience can't be more than your age")
    experience = int(input("Please, try again:"))
print(f"The candidate has {experience} years of experience")
pyth_exp = input("Have you any experience working with Python? Please, enter 'y' or 'n'")
while (pyth_exp != "n" and pyth_exp != "y"):
    pyth_exp = input("You should enter 'y' or 'n'. Please, try again:")
if pyth_exp == "n":
    print("Sorry, we are looking for a specialist with knowledge of Python. Good bye.")
elif experience <= 0:
    print("Sorry, we are looking for a specialist with experience. Good bye.")
else:
    phone_num = input("Thank you. We'll call you later. Enter your telephone number, please:")
    print("Good bye!")
