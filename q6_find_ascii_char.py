# q6_find_ascii_char.py

# get input
ASCII = input("Please enter ASCII value: ")

# check 
if ASCII.isnumeric():
    if int(ASCII) > 0 and int(ASCII) < 127:
        input_ASCII = int(ASCII)
        print("The character is", chr(input_ASCII), ".") # output result
    else:
        print("Invalid option!")
        ASCII = input("Please enter ASCII value:")
        if ASCII.isnumeric():
            input_ASCII = int(ASCII)
            print("The character is", chr(input_ASCII), ".")
else:
    print("Invalid option!")
    ASCII = input("Please enter ASCII value:")
    if ASCII.isnumeric():
        input_ASCII = int(ASCII)
        print("The character is", chr(input_ASCII), ".")
