# Python program for simple interest

def simple_interest(p, r, t):
    return p*r*t/100

principle = float(input("Enter principle : "))
rate = float(input("Enter rate : "))
time = float(input("Enter time : "))

print("Interest =", simple_interest(principle, rate, time))