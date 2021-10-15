import re

def calculator(number1, number2, operator):
    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        print(number1/number2)
    elif operator == "//":
        print(number1//number2)
    elif operator == "**":
        print(number1**number2)
    else:
        return False

def parse_input():
	numb1=""
	numb2=""
	ParseThis=input("Enter equation: ")
	In-num=re.findall(r'[0-9\.]+|[^0-9\.]+', ParseThis)
	print(calculator(In-num[0], In-num[2], in-num[1]))
    
