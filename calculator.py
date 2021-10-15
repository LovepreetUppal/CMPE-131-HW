import re

def calculator(number1, number2, operator):
	# adding floats to number 1 and 2
    number1=(number1)
    number2=(number2)
	# python operators for the calculator
    if(operator=="+"):
        return(number1+number2)
    if(operator=="-"):
        return(number1-number2)
    if(operator=="*"):
        return(number1*number2)
    if(operator=="/"):
        return(number1/number2)
    if(operator=="//"):
        return(number1//number2)
    if(operator=="**"):
        return(number1**number2)
    else:
        return False

def parse_input():
	# ask user for input
	ParseThis=input("Enter equation: ")
	# split the string 
	first_num = ParseThis.split()[0]
	second_num = ParseThis.split()[2]
	opera = ParseThis.split()[1]
	Num1= first_num
	Num2= second_num
	symbol = opera
	# sends the calculator the numbers and operator
	print(calculator(Num1, symbol, Num2))
    
