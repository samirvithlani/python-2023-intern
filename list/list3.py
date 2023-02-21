
no =0
flag = 1
data =[]
while True:
    no = int(input("Enter a number: "))
    data.append(no)
    flag = int(input("Do you want to continue? 1/0: "))
    if flag == 0:
        break

print("The list is: ", data)    
    