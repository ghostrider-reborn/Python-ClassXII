"""
    Function to check if a number is an armstrong number
"""

def is_armstrong(num):
    digs = Sum = 0
    t1_num = t2_num = num

    # To find number of digits
    while t1_num > 0:
        t1_num //= 10
        digs += 1

    # For the main part
    while t2_num > 0:
        dig = t2_num % 10
        Sum += dig ** digs
        t2_num //= 10

    if Sum == num: return "is"
    else: return "is not"

print("The number", is_armstrong(int(input("Enter the number > "))), "armstong number")
