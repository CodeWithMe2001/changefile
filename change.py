import os
import fileinput

files = []

for x in os.listdir():
    if x == "change.py" or x == "chars.txt":
        continue

    if os.path.isfile(x):
        files.append(x)

looking = True
while looking:
    text = input("Please input the text you would like to change: Enter 'exit' to quit: ")
    new = input("Please input the character you would like to replace with: ")

    for x in files:
        file = fileinput.FileInput(x, inplace=True, backup=False)
        for line in file:
            print(line.replace(text, new), end='')

    if text == "exit":
        looking = False
