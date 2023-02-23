def findArmstrng(no):
    rem= 0
    sum =0
    temp =no
    while no!=0:
        rem = no%10
        sum = sum + rem**3
        no = no//10
        
    if temp == sum:
        return True
    else:
        return False


no = int(input("Enter a number: "))
if findArmstrng(no):
    print("Armstrong")
else:
    print("Not Armstrong")    
        
        
        
    