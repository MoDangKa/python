# print("Hello world!")
# print("Ant\nBird\nCat")
# print("Hello" + " " + "Angela")

# print("Hello " + input("What is your name?") + "!")

# a = "Hello, World!"
# print(len(a))

# print(len(input("What is your name?")))

# --------------------------------------------------------

# username = input("What is your name?")
# length = len(username)
# print(username + " : " + str(length))


# --------------------------------------------------------

# glass1 = "milk"
# glass2 = "juice"

# print('You are not allowed to type the words "' + glass1 + '" or "' + glass2 + '"')
# print(f'You are not allowed to type the words "{glass1}" or "{glass2}"')

# --------------------------------------------------------

# print("Welcome to the Band Name Generator.")
# city = input("Which city did you grow up in?\n")
# pet = input("What is the name of a pet?\n")
# print("Your band name could be: " + city + " " + pet)

# --------------------------------------------------------

# mystery = 734_529.678
# print(mystery)

# --------------------------------------------------------

# print(type("abc"))
# print(type(123))
# print(type(3.14))
# print(type(True))

# print(int(123) + int(123))

# --------------------------------------------------------

# print(5 / 3)  # 1.6666666666666667
# print(5 // 3)  # 1
# print(2 * 3)  # 6
# print(2**3)  # 8

# --------------------------------------------------------

# height = 1.75
# weight = 75

# bmi = weight / (height**2)

# print(bmi)  # 24.489795918367346
# print(int(bmi))  # 24
# print(round(bmi))  # 24
# print(round(bmi, 2))  # 24.49

# --------------------------------------------------------

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}")

# --------------------------------------------------------

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height > 120:
#     print("You can ride the rollercoaster")

#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7")
#     else:
#         bill = 12
#         print("Adult tickets are $12")

#     want_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#     if want_photo == "y":
#         bill += 3

#     print(f"Your final bil is ${bill}")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# --------------------------------------------------------

# number_to_check = int(input("What is the number you want to check?"))

# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# --------------------------------------------------------

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ").upper()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
# extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("Invalid size selected. Please restart and choose S, M, or L.")
#     exit()

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}")

# --------------------------------------------------------

# print(not 5 == 5)
# print(False or True or False)

# --------------------------------------------------------

print('You\'re at a crossroad, where do you want to go? Type "left" or "right".')
