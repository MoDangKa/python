import sys

sys.path.append("D:/Fork/python")
from utils.utils import get_input


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formate_f_name = f_name.title()
    formate_l_name = l_name.title()
    return f"Result: {formate_f_name} {formate_l_name}"


print(format_name("AnGElA", "Yu"))  # Angela Yu
print(
    format_name(
        get_input("What is your first name?"), get_input("What is your last name?")
    )
)
