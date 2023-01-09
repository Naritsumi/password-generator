import string as str
import secrets

def generate_password(length: int, symbols: bool, uppercase: bool):
    combination = str.ascii_lowercase + str.digits

    if symbols:
        combination += str.punctuation

    if uppercase:
        combination += str.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

for _, index in enumerate(range(5)):
    password = generate_password(length=20, symbols=True, uppercase=True)
    print(index + 1, ">>", password)

#print(generate_password(length=20, symbols=True, uppercase=True))