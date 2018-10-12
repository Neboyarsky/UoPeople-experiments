#entering one of two operands
def input_number():
    n = None
    while n is None:
        try:
            n = float(input('Enter a number, not 0:\n'))  # user enters a number
        except ValueError:
            print('Not a valid number')
    return n

def input_operator():
    o = input('Enter operator: +, -, * or /:\n') #user enters operator
    while o != "+" and o != "-" and o != "*" and o != "/":
        o = input_operator()
    return(o)

num1 = input_number()
operator = input_operator()
num2 = input_number()

print (num1, operator, num2, '=', eval(str(num1)+operator+str(num2)))