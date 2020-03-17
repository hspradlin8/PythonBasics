# not a good way to verify passwords
# showing examples of While Loops
import sys

#all caps mean constant
MASTER_PASSWORD = 'opensesame'
password = input("Please enter the super secret password:   ")
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password. Try again:   ")
    attempt_count += 1
print("Welcome to secret town")    