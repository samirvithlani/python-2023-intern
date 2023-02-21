t1 = ("amit","raj","parth")
t1list = list(t1)
t1list.append("ajay")
t1 = tuple(t1list)
print(t1)

data = (["a","b"],["c","d"])
#data[0] = "amit" error....
print(data)
data[0].append("x")
print(data)
