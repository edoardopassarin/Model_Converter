
# first_name = 'Corey'
# last_name = 'Schafer'

# sentence = 'My name is {} {}'.format(first_name, last_name)
# print(sentence)

# sentence = f'My name is {first_name.upper()} {last_name.upper()}'
# print(sentence)

# ==================================================================

# person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
# print(sentence)

# sentence = f"My name is {person['name']} and I am {person['age']} years old"
# print(sentence)

# =================================================================

# calculation = f'4 times 11 is equal to {4 * 11}'
# print(calculation)

# =================================================================

# for n in range(1, 11):
#     sentence = f'The value is {n:03}'       # values are 0 padded to three digits
#     print(sentence)

# =================================================================

# pi = 3.14159265
# sentence = f'Pi is equal to {pi:.4f}'   # Now we have a floating point number with 4 digits after the .
# print(sentence)

# =================================================================

# from datetime import datetime
# birthday = datetime(1990, 1, 1)     # Jan 1st, 1990
#
# sentence = f'Jenn has a birthday on {birthday:%B %d, Y}'        # These are functions of datetime
# print(sentence)

# =================================================================

def equals_debugging():
    str_value = "other c"
    num_value = 123
    print(f'the value is {str_value}')      # functions normally
    print(f'{str_value = }')                # prints str_value = repr(str_value)
    print(f'{num_value % 2 = }')


def conversions():
    str_value = "other c"
    print(f'{str_value!r}')     # prints repr(str_value)


class MyClass:
    def __format__(self, format_spec) -> str:
        print(f'MyClass __format__ called with {format_spec=!r}')
        return "MyClass()"


def formatting():
    import datetime
    num_value = 123.456
    now = datetime.datetime.utcnow()
    print(f'{now = :%Y-%m-%d}')
    print(f'{num_value:.2f}')
    print(f'{MyClass():blah blah %%MYFORMAT%%}')

    nested_format = ".2f"
    print(f'{num_value:{nested_format}}')


# equals_debugging()
# conversions()
formatting()
