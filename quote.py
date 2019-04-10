import time

quote = "The greatest teacher failure is"

# The split method takes a string and turns it into a list
# Split will take a string and create elements based on a delimiter. (seperator)
words = quote.split()

for word in words:
    print(word)
    # the sleep method delays printing by the number in the argument
    time.sleep(.5)

travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]

print("travel expenses:")

week_number = 1
for week in travel_expenses:
    print("* Week #{}: ${}".format(week_number, sum(week)))
    week_number += 1