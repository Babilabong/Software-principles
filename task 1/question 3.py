def interceptPoint(first,sec):
    if type(first) != type(sec) or type(first) != tuple:
        return "Invalid input"

    if first[0] == sec[0]:
        if first[1] == sec[1]:
            return "same line"
        else:
            return "none"

    x=(first[1]-sec[1])/(sec[0]-first[0])
    y=first[0]*x+first[1]
    return (x, y)

print("according to Y = a1 * X + b2")
a1 = float(input("please enter a1: "))
b1 = float(input("please enter b1: "))
a2 = float(input("please enter a2: "))
b2 = float(input("please enter b2: "))
print("the solution is: ",str(interceptPoint((a1, b1), (a2, b2))))
