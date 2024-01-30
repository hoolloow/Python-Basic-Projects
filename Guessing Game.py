Name = input("Enter The Name To Be Predicted:- ")
clue = input("Enter The First Clue:- ")
clue2 = input("Enter The Second Clue:- ")
clue3 = input("Enter The Third Clue:- ")
Guess = ""
count=1
while Name.lower()!=Guess.lower() or count<=3:
    if (count==1):
        print(clue)
        Guess = input("Enter The Name:- ")
        count+=1
    elif(count==2):
        print(clue2)
        Guess = input("Enter THe Name:- ")
        count+=1
    elif(count==3):
        print(clue3)
        Guess = input("Enter The Name:- ")
        count+=1

    if(Name.lower()==Guess.lower()):
        print(f"You Guessed It Correct {Guess} it is !!")
    elif(Name.lower()!=Guess.lower() or count<=3):
        print("Try Again!!")
    else:
        print("Over!!")
