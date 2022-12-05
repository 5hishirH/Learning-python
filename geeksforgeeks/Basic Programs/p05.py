# Python program for compound interest

def compund_interest(p, r, t):
    return p*((1+r/100)**t) - p

principle = float(input("Enter a value : "))
rate = float(input("Enter rate : "))
time = float(input("Enter time : "))
interest = compund_interest(principle, rate, time)
print(str(rate) + "% compound interest of", principle,"in", time, "unit time is", interest)