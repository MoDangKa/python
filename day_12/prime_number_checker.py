import sys
import math

sys.path.append("D:/Fork/python")
from utils.utils import process_time


# The second
@process_time
def is_prime_v1(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


# The best
@process_time
def is_prime_v2(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += w
        w = 6 - w

    return True


# The third
@process_time
def is_prime_v3(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


is_prime_v1(
    55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
)
is_prime_v2(
    55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
)
is_prime_v3(
    55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
)
