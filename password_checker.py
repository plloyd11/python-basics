import sys

MASTER_PASSWORD = 'Buttz'

password = input("Please enter the super secret password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("You fuckin thief!")
    password = input("You wrong, dawg! Try again:  ")
    attempt_count += 1
print("Welcome to secret town, population you!")