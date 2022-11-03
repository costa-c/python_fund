# magic_number.py
# Guess the secrete number
# ask a number to user until guess  
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input('Number? '))
while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input('Number? '))

print('Well done, muggle! You are free now.')
