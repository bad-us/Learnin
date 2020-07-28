print("Hello this my calc")
number1 = float(input("Input number1 "))
number2 = float(input("Input number2 "))
sign = input("Mathematical Sign (+,-,*,/) ")

if sign in ('+','-','*','/'):
    if sign == "+":
        result = number1 + number2
    elif sign == "-":
        result = number1 - number2
    elif sign == "*":
        result = number1 * number2
    elif sign == "/":
        if number2 != '0':
            result = number1 / number2
        else:
            print("Division by zero")
    else:
        sign = input("Input Mathematical Sign ")

print("You example: " + f"{number1}" + f"{sign}" + f"{number2} " + "Result: " + f"{result}")

word = input("Input text")
print(word)

# print(f"Input symbols {digital}, {word}")
