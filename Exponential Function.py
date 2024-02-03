Base = int(input("Enter The Base Of The Function:- "))
Power = int(input("Enter The Power To Which It Needs To Be Calculated:- "))

count=1

for i in range(1,Power+1):
    count*=Base

print(count)

