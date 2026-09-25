#Marcus Ee
#math_interpreter
#user gives a single operation math equation and computer solves it



def mathOperation(op):
    match op:
        case "+":
            print(float(equation[0]) + float(equation[2]))
        case "-":
            print(float(equation[0]) - float(equation[2]))
        case "*":
            print(float(equation[0]) * float(equation[2]))
        case "/":
            print(float(equation[0]) / float(equation[2]))
        case _:
            print("That is not a valid operation!")
            
equation = input("Equation (# operator #): ").split(" ")
mathOperation(equation[1])
