#.write a python script to enter any number, if its is integer number,then check its armstrong or not .print appropriate message if its is not armstrong


n=input("Enter a number!!")
if(n.isdigit()):
    n=int(n):
    r=0
    sm=0
    a=n
    while(n!=0):
        r=n%10
        sm=sm+(r**3)
        n//=10
    if(a==sm):
        print(f"The number {a} is an armstrong number!")
    else:
        print(f"The number {a} is not an armstrong number!")
else:
    print(f"The given input {n} is not valid number!!")












