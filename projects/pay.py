import math

def split_check(total, number_of_peeps):
    if number_of_peeps <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_peeps)

try:
    total_due = float(input("What is the total?  "))
    number_of_peeps = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_peeps )
except ValueError as err:
    print("Oh no! That's not a valid value, you fucking dolt!")
    print("({})".format(err))
else:
    print("Each person owes ${}" .format(amount_due))