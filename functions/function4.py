def getData(*args,no):
    print(args)
    print("no...",no)
    for i in args:
        print(i)

def getData1(*args):
    print(args)
    #print("no...",no)
    for i in args:
        print(i)

getData1(15,25,96)    
    