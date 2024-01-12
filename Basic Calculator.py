import math

Operation = input("Enter The Symbol To Perform Operation(pow for power):-   ")

if(Operation.lower()=="pow"):
    Base = int(input("Enter The Value Of Base:- "))
    Exp = int(input("Enter The Value Of Exponential:- "))
    print(f"You Performed Power Operationn {pow(Base, Exp)}")

elif(Operation.lower()!="pow"):
    if (not Operation == ""):
        First = int(input("Enter Your First Number:- "))
        Second = int(input("Enter Your Second Number:- "))
        if (Operation == "+"):
            print(f"You Performed Addition {First + Second}")
        elif (Operation == "-"):
            print(f"You Performed Subtraction {First - Second}")
        elif (Operation == "*"):
            print(f"You Performed Multiplication {First * Second}")
        elif (Operation == "/"):
            Step = (input("What You Want To Get Float Or Int As Ouput:- "))
            try:
                if (Step.lower() == "float"):
                    print(f"You Wanted Float {First / Second}")
                elif (Step.lower() == "int"):
                    print(f"You Wanted Integer As Output {First // Second}")
            except ZeroDivisionError:
                print("The Value Is Being Divided By Zero")
    else:
        print("Enter Some Value!!")





