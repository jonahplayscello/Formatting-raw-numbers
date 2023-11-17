"""
Jonah Hosea 
Pltw CSE
11/13/23

revised 11/14/23 to not use format function and 
restart if they enter something other than a b or c
and to let the user go agian if they want to 

revised 11/15/23 to make some comments more clear 

revised 11/16/23 to trauncate the number for scientific notation 
and to make the currency add commas to the output

here is a short definition of "mantissa"
In the context of scientific notation, the mantissa is the part of a
number that represents its significant digits. It is the coefficient
that is multiplied by the base raised to the exponent in scientific
notation. For example, in the number "a × 10^b," "a" is the mantissa.
"""
# adds commas to numbers
# takes an int as a input and provides a int result
def add_commas(number):
    str_number = str(number)
    result = ""
    count = 0

    for digit in reversed(str_number):
        if count == 3:
            result = "," + result
            count = 0
        result = digit + result
        count += 1

    return result

# converts a number to scientific notation 
# takes an int input then provides a string output 
def scientific_notation(number):
    if number == 0:
        return "0"

    sign = 1 if number > 0 else -1
    number = abs(number)

    # Find the exponent by counting the number of decimal places
    exponent = 0
    while number < 1:
        number *= 10
        exponent -= 1
    while number >= 10:
        number /= 10
        exponent += 1

    # Computes the mantissa 
    # look at top for mantissa definition 
    mantissa = round(number,4)
    number -= mantissa

    # Convert mantissa and exponent to strings
    mantissa_str = str(sign * mantissa)
    exponent_str = str(exponent)

    # finding the result 
    result = mantissa_str + " x 10^" + exponent_str
    
    return result

# converts a number to currency format 
# takes a float input and provides a string output
def convert_currency(number):
    dollars = int(number)
    cents = int((number - dollars) * 100)

    # adds commas to the dollars varibal 
    # this code is from the add_commas function 
    result = ""
    count = 0
    str_dollars = str(dollars)
    for digit in reversed(str_dollars):
        if count == 3:
            result = "," + result
            count = 0
        result = digit + result
        count += 1
    dollars = result

    # Manually formatting the output 
    result = "$" + str(dollars) + "."
    if cents < 10:
        result += "0" + str(cents)
    else:
        result += str(cents)
    
    return result

# the while loop allows the user to do it agian easily 
while True:
    # Ask the user which operation they want to do
    print("What do you want to do? ")
    print("A. Add commas")
    print("B. Scientific notation")
    print("C. Convert currency")
    answer = input("> ").upper()  # Convert input to uppercase 

    # Handle invalid input
    if answer not in ["A", "B", "C"]:
        print("Please only enter A, B, or C")
        print(" ")
    else:
        # If they enter A, then enter a number it will add commas in the correct places
        if answer == "A":
            user_number = int(input("Enter your number: "))
            print("Original number: " + str(user_number) + " Formatted Number: " + str(add_commas(user_number)))

        # If they enter B, then enter a number, it will convert the number to scientific notation
        elif answer == "B":
            user_number = int(input("Enter your number: "))
            print("Original number: " + str(user_number) + " Formatted Number: " + str(scientific_notation(user_number)))

        # If they enter C, then enter a number, it will round to the nearest cent and format as currency
        elif answer == "C":
            user_number = float(input("Enter your number: "))
            if user_number < 0:
                print("You cannot enter a negative number!")
            else:
                print("Original number: " + str(user_number) + " Formatted Number: " + str(convert_currency(user_number)))
        
        # Ask if the user wants to run the program again
        print(" ")
        another_attempt = input("Do you want to format more numbers? (Y/N): ").upper()
        if another_attempt == "Y":
            print(" ")
            continue

        elif another_attempt == "N":
            break
        else:
            print(" ")
            print("Please only enter Y or N!")
            break