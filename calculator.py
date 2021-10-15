import re

def calculator(number1, number2, operator):
    number1=float(number1)
    number2=float(number2)
    if(operator=="+"):
        return(float(number1+number2))
    if(operator=="-"):
        return(float(number1-number2))
    if(operator=="*"):
        return(float(number1*number2))
    if(operator=="/"):
        return(float(number1/number2))
    if(operator=="//"):
        return(number1//number2)
    if(operator=="**"):
        return(float(number1**number2))
    else:
        return False

def parse_input():
	numb1=""
	numb2=""
	ParseThis=input("Enter equation: ")
	In-num=re.findall(r'[0-9\.]+|[^0-9\.]+', ParseThis)
	print(calculator(In-num[0], In-num[2], In-num[1]))
    
