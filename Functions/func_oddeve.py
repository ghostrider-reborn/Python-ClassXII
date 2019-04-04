"""
    Write a function to check if a num is odd or even
"""

def OddEve(num):
    if num % 2 == 0: return "even"
    return "odd"

print("The number is", OddEve(int(input("Enter num > "))))
