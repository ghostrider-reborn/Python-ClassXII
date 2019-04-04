"""
    Function to check if a number is a perfect number
"""

def is_perfect(num):
    Sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            Sum += i

    if Sum == num: return "is"
    else: return "is not"

print("The number", is_perfect(int(input("Enter the number > "))), "a perfect number")
