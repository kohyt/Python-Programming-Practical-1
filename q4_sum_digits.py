# q4_sum_digits.py
# calculate the sum of the digits for integers between 0 and 1000

# get input
input_number = input("Enter an integer between 0 and 1000:")
    
# calculate sum of digits
if input_number.isnumeric():
    number = int(input_number)
    if number > 0 and number < 1000:
        result = 0
        while number != 0:
            result = result + number % 10
            number = number // 10
        print ("Sum of digits:", result)
            
    else:
        print("Invalid input!")
        input_number = input("Enter an integer between 0 and 1000:")
        if input_number.isnumeric():
            number = int(input_number)
            if number > 0 and number < 1000:
                result = 0
                while number != 0:
                    result = result + number % 10
                    number = number // 10
                print ("Sum of digits:", result)
else:
    print("Invalid input!")
    input_number = input("Enter an integer between 0 and 1000:")
    if input_number.isnumeric():
        number = int(input_number)
        if number > 0 and number < 1000:
            result = 0
            while number != 0:
                result = result + number % 10
                number = number // 10
            print ("Sum of digits:", result)


