import string 
import secrets

rangeInput = int(input())
rangeLength = int(input())
symbolsOrNot = bool(input())
uppercaseOrNot = bool(input())

def generate_password(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

for _, index in enumerate(range(rangeInput)):
    password = generate_password(length=rangeLength, symbols=symbolsOrNot, uppercase=uppercaseOrNot)
    print(index + 1, ">>", password)
