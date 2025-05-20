def is_leap_year(year):
    """
    Determine if a given year is a leap year.

    Leap year rules:
    1. If a year is divisible by 400 → LEAP YEAR
    2. If a year is divisible by 100 → NOT leap year
    3. If a year is divisible by 4 → LEAP YEAR
    4. Else → NOT leap year

    Args:
        year (int): The year to check

    Returns:
        bool: True if leap year, False otherwise
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
