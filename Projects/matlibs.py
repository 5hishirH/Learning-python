# string concatenation (how to put strings together)
# suppose we want to create a string "Happiness is a journey, not a destination." 

# shishir = "not a destination."

# a few ways to do it

# print("Happiness is a journey,", shishir)
# print("Happiness is a journey, " +shishir)
# print("Happiness is a journey, {}" .format(shishir))
# print(f"Happiness is a journey, {shishir}")

adjective = input("Enter an adjective : ")
verb1 = input("Enter a verb : ")
verb2 = input("Enter another verb : ")
famous_person = input("Famous person : ")

matlibs = f"Computer programming is so {adjective}!. It makes me so exicited all the time because\
\nI love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(matlibs)