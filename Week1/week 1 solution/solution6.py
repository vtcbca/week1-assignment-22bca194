#.write a python script to enter any sting and print only part of string .Take input of start character from user.



s=input("Enter a string:")
t=int(input("Enter start position:"))
e=int(input("Enter end position:"))

print(f"The part of the string '{s}' is '{s[t-1:e:]}'")