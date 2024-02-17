
def onlyPositive(f):
    def wrapper(x):
        x = abs(x)
        return f(x)

    return wrapper

def f1(x):
    return x + 1

g = onlyPositive(f1)
print("the absolut value + 1 is: ",g(int(input("please enter integer number: "))))