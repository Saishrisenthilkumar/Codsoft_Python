def calculator():
    n1=int(input("Enter the first number"))
    n2=int(input("Enter the second number"))
    op=input("Please enter the math operation you want")
    if op=='+':
        print(n1+2)
    elif op=='-':
        print(n1-n2)
    elif op=='*':
        print(n1*n2)
    elif op=='/':
        print(n1/n2)
    else:
        print("Invalid operator, please run the code again")
    rerun=input("Do you want to run the programme again? Y/N")
    if rerun.upper()=='Y':
        calculator()
    elif rerun.upper()=='N':
        print("Bye bye")
    else:
        again()
calculator()