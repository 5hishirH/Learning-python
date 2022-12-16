# A difference function, which subtracts one list from another and returns the result.
def array_diff(a, b):
    for i in b:
        for j in range(a.count(i)):
            a.remove(i)

    return a


# driver code
p = [1, 2, 2, 2, 3, 5, 8, 11]
q = [2, 5, 7]

print(array_diff(p, q))