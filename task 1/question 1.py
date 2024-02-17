def factorSum(number):

    if number <= 1 and type(number) != int:
        return 0

    def div_loop():
        for i in range(2,number):
            if number % i == 0:
                return i
        return number

    arr = []

    while(number != 1):
        first_factor = div_loop()
        number = int(number/first_factor)
        flag = False
        for i in range(len(arr)):
            if arr[i] == first_factor:
                flag = True
                break
        if flag == False:
            arr.append(first_factor)

    return sum(arr)

print("the sum of all the first factors is: ",factorSum(int(input("please enter integer number bigger than 1: "))))
