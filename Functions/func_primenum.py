"""
    Function to check if a number is a prime number
"""

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return "not prime"
            break
    
    return "prime"

print("The number is", is_prime(int(input("Enter the number > "))))
        
