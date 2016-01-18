# q3_miles_to_kilometre.py
# miles to kilometres converter

# get input
miles = input("Enter here(miles):")

# check
if miles.isnumeric():
    input_miles = int(miles)
    kilometres = input_miles * 1.60934
# output result
    print("{0} miles = {1:0.3f} kilometres".format(input_miles,kilometres))
else:
    print("Invalid input!")
    miles = input("Enter here(miles):")
    if miles.isnumeric():
        input_miles = int(miles)
        kilometres = input_miles * 1.60934
        print("{0} miles = {1:0.3f} kilometres".format(input_miles,kilometres))
    
