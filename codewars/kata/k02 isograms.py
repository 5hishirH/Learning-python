# is isogram
def is_isogram(string):
    #convert the string into a list
    lst = list(string.lower())

    # check frequency of each element in the list
    for i in lst:
        if lst.count(i) > 1:
            return False
    return True