# Rearrange the digits of a number in descending order

def descending_order(num):
    # convert the number into string
    num = str(num)

    lst = []
    for i in num:
        lst.append(int(i))

    # sort the list
    lst.sort()
    lst.reverse()

    # concatenate string
    newNum = ""
    for i in lst:
        newNum += str(i)

    # convert to integer

    return int(newNum)

# driver code
number = int(input("Enter a number : "))
sorted_num = descending_order(number)
print("Digits in descending order :", sorted_num)