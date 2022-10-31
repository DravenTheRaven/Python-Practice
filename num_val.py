
def float_validate():
    num = input('Enter a number: ')
    try:
        float_num = float(num)
    except:
        print("Please enter a valid number")
        float_num = num_val()
        return float_num
    else:
        return float_num

num_val()

def yes_no_validation(var_str, val_op_str):

    check = input(f"{var_str}")
    if check == "y":
        float_value = float_validate(var_str)
        return float_value
    elif check == "n":
        float_value = 0
        return float_value
    else:
        print(f"Please enter a valid option")
        float_value = yes_no_validation(var_str, val_op_str)
        return float_value

def simple_y_n(var_str):
    check = input(f"{var_str}")
    if check == "y":
        return check
    elif check == "n":
        return check
    else:
        print("Please enter a valid option")
        check = simple_y_n(var_str)

        (r'$\.\d\d')
import re

str = 'an example word:0.44'
match = re.search((r'$\.\d\d'), str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')
