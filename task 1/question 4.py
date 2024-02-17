def printNumbers(start,stop,without):
    if start == stop:
        if start == without:
            return
        else:
            print(start)
            return
    elif start > stop:
        if start == without:
            printNumbers(start-1,stop,without)
        else:
            print(start ,end=",")
            printNumbers(start-1,stop,without)
    else:
        if start == without:
            printNumbers(start+1,stop,without)
        else:
            print(start ,end=",")
            printNumbers(start+1,stop,without)

    return

start = int(input("enter starting number: "))
stop = int(input("enter ending number: "))
without = int(input("enter without number: "))
printNumbers(start,stop,without)