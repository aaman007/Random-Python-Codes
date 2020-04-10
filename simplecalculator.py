#Returns the sum of num1 and num2
def add(num1,num2):
    return num1 + num2
    
#Return the substraction of num1 and num2
def sub(num1,num2):
    return num1 - num2

#Returns the multiply of num1 and num2
def mul(num1,num2):
    return num1 * num2

#Returns the division of num1 and num2
def div(num1,num2):
    return num1 / num2

#MAIN FUNCTION
def main():
    for i in range(7):
        text = input("What operation do wanna do[+,-,*,/]\n")
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        if(text == '+'):
            print(add(num1,num2))
        elif(text == '-'):
            print(sub(num1,num2))
        elif(text == '*'):
            print(mul(num1,num2))
        else:
            print(div(num1,num2))

main()
