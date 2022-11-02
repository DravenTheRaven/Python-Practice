import re


def add_zeros(price):
    str = str(price)
    match = re.search('\.\d\d$', str)
# If-statement after search() tests if it succeeded
    if match:
        return str ## 'found word:cat'
    else:
        return str + '0'
