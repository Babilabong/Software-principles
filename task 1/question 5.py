def listProduct(list1, list2):

    if type(list1) != type(list2) or type(list1) != list or len(list1) != len(list2):
        return "Invalid Input"
    for i in range(len(list1)):
        if list1[i] < 0 or list2[i] < 0:
            return "Invalid Input"

    newList = []
    size2=len(list2)
    for i in range(size2):
        for j in range(list2[i]):
            newList.append(list1[i])

    return newList


f_list = []
s_list = []
size = int(input("Enter size of list: "))
for i in range(size):
    f_list.append(int(input("Enter element " + str(i+1) + " for first list: ")))
    s_list.append(int(input("Enter element " + str(i+1) + " for second list: ")))

print(listProduct(f_list, s_list))

