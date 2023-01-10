import string 
import secrets
import os

print('\nGoing to generate a unique password...\n')
rangeInput = 1
rangeLength = int(input("Number of characters: "))

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

def evaluateSymbolsOrNot():
    symbols = input("Do you want to include Symbols? [Y/N] ")
    if symbols == "Y":
        return True
    if symbols == "N":
        return False
    return symbols

symbolsOrNot = evaluateSymbolsOrNot()

def evaluateUppercaseOrNot():
    uppdercase = input("Do you want to include Uppercase letters? [Y/N] ")
    if uppdercase == "Y":
        return True
    if uppdercase == "N":
        return False
    return uppdercase

uppercaseOrNot = evaluateUppercaseOrNot()

for _, index in enumerate(range(rangeInput)):
    password = generate_password(length=rangeLength, symbols=symbolsOrNot, uppercase=uppercaseOrNot)
    print(index + 1, ">>", password)

command = 'echo ' + password.strip() + '| clip'
#os.system(command)

print('Password copied to clipboard')