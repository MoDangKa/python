import random

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# -----------------------------------------------------------------------

# student_scores = [random.randint(0, 100) for _ in range(50)]
# print(student_scores)

# total_exam_score = sum(student_scores)
# print(f"Total : {total_exam_score}")

# max_score = max(student_scores)
# print(f"Max : {max_score}")

# min_score = min(student_scores)
# print(f"Min : {min_score}")

# average_score = sum(student_scores) / len(student_scores)
# print(f"Average : {average_score:.2f}")

# -----------------------------------------------------------------------

numbers = []
for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        numbers.append("FizzBuzz")
    elif number % 3 == 0:
        numbers.append("Fizz")
    elif number % 5 == 0:
        numbers.append("Buzz")
    else:
        numbers.append(number)

print(numbers)
