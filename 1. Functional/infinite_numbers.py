history = []

def infinite():
    num = 0
    while True:
        yield num
        num +=1

for x in infinite():
    history.append(x)
    print(x,history)