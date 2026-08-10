m1=int(input("Enter marks 1: "))
m2=int(input("Enter marks 2: "))
m3=int(input("Enter marks 3: "))

#check for total percentage
total_percentage= ((m1+m2+m3)/300)*100

if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are pass", total_percentage)
    
else:
    print("You are fail, try next year!", total_percentage)