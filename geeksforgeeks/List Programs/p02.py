# Python program to swap two elements in a list

def swap_ele(newlst, a, b):
    tp = newlst[a], newlst[b]
    newlst[b], newlst[a] = tp

    return newlst

# driver code
lst = []
n = int(input("Enter the number of elements : "))
for i in range(0, n):
    lst.append(input())

print("Enter swap positons")
p1 = int(input("Position 1 : "))
p2 = int(input("Position 2 : "))
lst = swap_ele(lst, p1, p2)
print(lst)