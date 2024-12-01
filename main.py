import random
import pyperclip
import time
import os
import string
import sys

generatedPassword = ""
characters = string.punctuation + string.ascii_letters + string.digits
txtPath = "generator_path.txt"


question = input("Do you want to use a custom path? (y/n): ").lower()
path = ""

if question == "y":
    pathQuestion = input("Enter path: ")
    if os.path.isdir(pathQuestion):
        print("Path assigned successfully!")
        path = pathQuestion
        with open(txtPath, 'w') as file:
            file.write(path)
    else:
        print("The entered path isn't a valid directory.")
        time.sleep(3)
        sys.exit()
elif question == "n":
    if os.path.isfile(txtPath):
        print("Default path assigned from txt.")

    else:
        print("No path found.")
        time.sleep(3)
        sys.exit()

try:
    letters = int(input("How much characters should the password be? "))
except ValueError:
    print("Value entered wasn't an integar.")
    sys.exit()


for l in range(letters):
    generatedPassword += random.choice(characters)

pyperclip.copy(generatedPassword)
print("Password generated: "+generatedPassword+"\nPassword has been copied to clipboard!")


fileQuestion = input("Do you want to put the password in a file? (y/n): ").lower()

if fileQuestion == "y":
    pass
elif fileQuestion == "n":
    print("Closing program...")
    time.sleep(2)
    sys.exit()

fileName = input("File name: ")

with open(path + "\\" + fileName + ".txt", 'w') as file:
    file.write(generatedPassword)
    

print("File Created successfully!")
input("\nPress Enter to exit...")

