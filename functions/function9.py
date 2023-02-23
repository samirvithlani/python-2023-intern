def test():
    yield 100
    yield 200
    yield 300
    yield 400
    

# x = test()    
# print(x)

for i in test():
    print(i)