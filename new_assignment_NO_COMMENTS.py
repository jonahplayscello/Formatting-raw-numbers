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

def scientific_notation(number):
    if number == 0:
        return "0"

    sign = 1 if number > 0 else -1
    number = abs(number)

    exponent = 0
    while number < 1:
        number *= 10
        exponent -= 1
    while number >= 10:
        number /= 10
        exponent += 1

    mantissa = round(number, 4)
    number -= mantissa

    mantissa_str = str(sign * mantissa)
    exponent_str = str(exponent)

    result = mantissa_str + " x 10^" + exponent_str
    
    return result

def convert_currency(number):
    dollars = int(number)
    cents = int((number - dollars) * 100)

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

    result = "$" + str(dollars) + "."
    if cents < 10:
        result += "0" + str(cents)
    else:
        result += str(cents)
    
    return result

while True:
    print("What do you want to do? ")
    print("A. Add commas")
    print("B. Scientific notation")
    print("C. Convert currency")
    answer = input("> ").upper()

    if answer not in ["A", "B", "C"]:
        print("Please only enter A, B, or C")
        print(" ")
    else:
        if answer == "A":
            user_number = int(input("Enter your number: "))
            print("Original number: " + str(user_number) + " Formatted Number: " + str(add_commas(user_number)))

        elif answer == "B":
            user_number = int(input("Enter your number: "))
            print("Original number: " + str(user_number) + " Formatted Number: " + str(scientific_notation(user_number)))

        elif answer == "C":
            user_number = float(input("Enter your number: "))
            if user_number < 0:
                print("You cannot enter a negative number!")
            else:
                print("Original number: " + str(user_number) + " Formatted Number: " + str(convert_currency(user_number)))
        
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
