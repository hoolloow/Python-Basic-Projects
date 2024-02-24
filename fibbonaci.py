def number(n):
    if n<=1:
        return(n)
    else:
        return (number(n-1)+ number(n-2))


a = int(input("Enter The First Number:- "))
if(a<0):
    print("Invalid")
else:
    for i in range(0, a):
        print(number(i))

