age = int(input("Enter your age"))

if age>=18:
    print("you are eligible to vote")
    
    if age>=21:
        print("you are eligible to marry")
    else:
        print("you are not eligible to marry")    
        
else:
    print("you are not eligible to vote")
    if age>=5:
        print("you are eligible to study")
    else:
        print("stay at home !!!")            