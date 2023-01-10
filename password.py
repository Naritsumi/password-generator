import string 
import secrets
import os

yes_choices = ['YES', 'Y', 'y', 'yes']
no_choices = ['NO', 'N', 'n', 'yes']

def menu():
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

    #Se podría optimizar y unificar en un solo método
    def evaluateSymbolsOrNot():
        symbols = input("Do you want to include Symbols? [Y/N]: ")
        if symbols in yes_choices:
            return True
        elif symbols in no_choices:
            return False
        else:
            print('Type Y or N')
        return symbols

    symbolsOrNot = evaluateSymbolsOrNot()

    def evaluateUppercaseOrNot():
        uppercase = input("Do you want to include Uppercase letters? [Y/N]: ")
        if uppercase in yes_choices:
            return True
        elif uppercase in no_choices:
            return False
        else:
            print('Type Y or N')        
        return uppercase

    uppercaseOrNot = evaluateUppercaseOrNot()

    for _, index in enumerate(range(rangeInput)):
        password = generate_password(length=rangeLength, symbols=symbolsOrNot, uppercase=uppercaseOrNot)
        print(index + 1, ">>", password)    

    if len(password) < 8 or password.lower() == password or password.upper() == password or password.isalnum()\
            or not any(i.isdigit() for i in password):
        print('\nYour password is WEAK')

    else:
        print('\nYour password is STRONG')     

    def addToClipBoard(text):
        try:        
            command = 'echo | set /p nul=' + text.strip() + '| clip'   
            os.system(command)            
            print("Check your clipboard")
        except:
            print("An exception occurred copying the password")

    addToClipBoard(password)

    def regeneratePassword():
        regenerate = input("\nDo you want to regenerate password? [Y/N] ")
        if regenerate in yes_choices:
            return menu()     
        elif regenerate in no_choices:        
            print('Ok, bye :)\n')
            exit()
        else:
            print('Type Y or N')

    regeneratePassword()

menu()