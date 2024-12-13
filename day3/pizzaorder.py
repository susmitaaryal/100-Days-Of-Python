print("WELCOME TO PYTHON PIZZA DELIVERIES!!!")
size = input("what size do you want? S,M,L : ")
add_pepperoni= input("do you want pepproni? Y,N : ")
extra_cheese= input("do you want extra cheese? Y,N: ")

bill=0

if size == "S":
    bill = bill +15
elif size == "M":
    bill = bill + 20
elif size == "L":
    bill = bill + 25
    
if add_pepperoni == "Y":
    if size == "S":
        bill = bill +2
    else:
        bill = bill +3 
        
if extra_cheese == "Y":
    bill = bill+1
    
print (f"you final bill is ${bill}")


    
    