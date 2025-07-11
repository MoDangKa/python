# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


print("Welcome to the PyPassword Generator!")

# Method 1 : Set the number of letters, symbols and numbers
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# Method 2 : Set the number of characters
nr_characters = int(input("How many characters would you like in your password?\n"))

nr_letters = random.randint(2, nr_characters - 2)
nr_symbols = random.randint(2, nr_characters - 2)
nr_numbers = nr_characters - (nr_letters + nr_symbols)

print(f"Random letters: {nr_letters}")
print(f"Random symbols: {nr_symbols}")
print(f"Random numbers: {nr_numbers}")

# -----------------------------------------------------------------------

# Eazy Level - Order not randomised:
# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

# -----------------------------------------------------------------------

# Hard Level - Order of characters randomised:
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)  # random order in a list
print(password_list)

password = ""
for char in password_list:
    password += char

password2 = "".join(password_list)

print(f"Your password is: {password}")
print(f"Your password2 is: {password2}")
