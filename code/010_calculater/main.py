# Build a calculater

# libraries
from time import sleep


print("welcome to calculater")
sleep(1)

def multiply(n1, n2):
    return n1*n2

def substract(n1, n2):
    return n1-n2

def division(n1, n2):
    return n1/n2

def sum_(n1, n2):
    return n1+n2

operations = {
    "*": multiply,
    "-": substract,
    "/": division,
    "+": sum_
}

def user_input():
    # input first number
    f_number = float(input("First Number: "))
    # input operator
    operator = input("Type the operator (+ | - | / | *): ")
    # input second number
    s_number = float(input("Second Number: "))
    return f_number, operator, s_number


def main():
    # output the result
    # condition for chose the operator
    fn, op, sn = user_input()
    calc_func = operations[op]
    result = calc_func(fn, sn)
    print(f"{fn} {op} {sn} = {result}")
            
# ask for restart or close
if __name__=="__main__":
    calc = True
    while calc:
        main()
        again = input("Do you would like calculate another numbers? Yes/No: ").lower()
        if again in ("yes", "y"):
            continue
        else:
            calc = False
            print("Finished! ")
            break