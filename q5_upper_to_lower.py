# q5_upper_to_lower.py
# convert upper case to lower case]

# get input
character = input("Please enter a letter here:")

# check
while character.isnumeric():
    print("Invalid input!")
    character = input("Please enter a letter here:")

while ord(character) >= 97 and ord(character) <=122:
    print("Invalid input!")
    character = input("Please enter a letter here:")
    while character.isnumeric():
        print("Invalid input!")
        character = input("Please enter a letter here:")

if ord(character) >= 65 and ord(character) <= 90:
    result = chr(ord(character) + 32)
    print(result)


    

##
##65-90
##uppercase
##
##97-122
##lowercase
