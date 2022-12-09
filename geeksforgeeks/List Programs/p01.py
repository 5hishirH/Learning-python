# Python program to interchange first and last element in a list

def interchange1L(newlist):
    temp = newlist[0]
    newlist[0] = newlist[- 1]   # [-1] indicates last element
    newlist[- 1] = temp

    return newlist

# driver code
lst = []
n = int(input("Enter numbers of elements : "))
for i in range(0, n):
    lst.append(input())

lst = interchange1L(lst)
print("List =", lst)