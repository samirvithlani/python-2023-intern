# for i in range(10,0,-1):
#     print(i)
    
a = int(input("Enter a number: "))
sum=1

# for i in range(1,a):
#     if i %2 ==0:
#         print(i)    

# for i in range(1,11):
#     print(a ," * ", i ," = ", a*i)


for i in range(1,a+1):
    #1  = 1 * 1
    #2 = 1 * 2 =2
    #2 = 2 *3 = 6
    #6 = 6 * 4 = 24
    #24 = 24 * 5 = 120
    sum = sum * i
    

print(sum)    
    