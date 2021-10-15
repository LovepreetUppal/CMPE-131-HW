import re

def calculator(number1, number2, operator):
	# adding floats to number 1 and 2
    number1=float(number1)
    number2=float(number2)
	# python operators for the calculator
    if(operator=="+"):
        return(float(number1+number2))
    if(operator=="-"):
        return(float(number1-number2))
    if(operator=="*"):
        return(float(number1*number2))
    if(operator=="/"):
        return(float(number1/number2))
    if(operator=="//"):
        return(float(number1//number2))
    if(operator=="**"):
        return(float(number1**number2))
    else:
        return False

def parse_input():
	ParseThis=input("Enter equation: ")
	first_num = ParseThis.split()[0]
	second_num = ParseThis.split()[2]
	opera = ParseThis.split()[1]
	Num1= first_num
	Num2= second_num
	symbol = opera
	
	
	#In-num=re.findall(r'[0-9\.]+|[^0-9\.]+', ParseThis)
	print(calculator(Num1, symbol, Num2))
    
