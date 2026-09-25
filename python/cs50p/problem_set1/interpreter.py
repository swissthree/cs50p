#Marcus Ee
#math_interpreter
#user gives a single operation math equation and computer solves it



def mathOperation(op):
    match op:
        case "+":
            print(float(equation.split()[0]) + float(equation.split()[2]))
        case "-":
            print(float(equation.split()[0]) - float(equation.split()[2]))
        case "*":
            print(float(equation.split()[0]) * float(equation.split()[2]))
        case "/":
            print(float(equation.split()[0]) / float(equation.split()[2]))
        case _:
            print("That is not a valid operation!")
            
equation = input("Equation: ").split(" ")
mathOperation(equation.split()[1])
