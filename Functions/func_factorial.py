"""
    Function to find the factorial of a number
"""

def factorial(num):
    fac = num
    for i in range(1, num):
        fac *= i

    if num is 0: return 1
    return fac

print("\nThe factorial of the number is", factorial(int(input("Enter a number > "))))
