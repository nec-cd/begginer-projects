def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multipy(n1, n2):
    return n1*n2

def divide (n1, n2):
    return n1/n2

calc_func= {"+" : add,
            "-" : substract,
            "*" : multipy,
            "/": divide
}

def calc_us(first_num,func_op,second_num):
    if func_op == "+":
        print(f"{first_num} + {sec_num} = {calc_func[func_op](first_num, sec_num)}")
    elif func_op == "-":
        print(f"{first_num} - {sec_num} = {calc_func[func_op](first_num, sec_num)}")
    elif func_op == "*":
        print(f"{first_num} * {sec_num} = {calc_func[func_op](first_num, sec_num)}")
    elif func_op == "/":
        print(f"{first_num} / {sec_num} = {calc_func[func_op](first_num, sec_num)}")


cont_calc= True

cont_new= True

while cont_calc:
    while cont_new:
        first_num= float(input("Enter the first number: "))
        for operation in calc_func:
            print(operation)
        func_op= input("Enter the operation: ")
        sec_num= float(input("Enter the second number: "))

        calc_us(first_num,func_op,sec_num)
        result = calc_func[func_op](first_num, sec_num)

        continue_or_not = input("Do you want to continue working with the previous result? Type 'y' for yes or 'n' for no:")
        if continue_or_not == "n":
            cont_new= True
            cont_or_close = input(
                "Do you want to continue working with the calculator? Type 'y' for yes or 'n' for no:")
            if cont_or_close == "y":
                print("\n"*20)
            else:
                cont_calc = False
                break
        else:
            cont_new= False


    while not cont_new:
        first_num = result
        for operation in calc_func:
            print(operation)
        func_op = input("Enter the operation: ")
        sec_num = float(input("Enter the second number: "))

        calc_us(first_num, func_op, sec_num)
        result = calc_func[func_op](first_num, sec_num)

        continue_or_not = input(
            "Do you want to continue working with the previous result? Type 'y' for yes or 'n' for no:")
        if continue_or_not == "n":
            cont_new = True
            cont_or_close = input("Do you want to continue working with the calculator? Type 'y' for yes or 'n' for no:")
            if cont_or_close == "y":
                print("\n" * 20)
            else:
                cont_calc = False
                break
        else:
            cont_new = False