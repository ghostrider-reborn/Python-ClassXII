"""
    Function to check if a given number is a palindrome
"""

def is_palindrome(num):
    orig_num = num
    rev_num = 0
    
    while num > 0:
        dig = num % 10
        num //= 10
        rev_num = rev_num*10 + dig

    if orig_num == rev_num:
        return "is"

    return "is not"

print("\nThe given number", is_palindrome(int(input("Enter a number > "))), "a palindrome number")
