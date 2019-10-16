"""
    RECURSIVE FUNCTIONS
"""

def sumOfN(n):
    ''' Find sum of first 'n' natural numbers '''
    if n == 1: return 1
    return n + sumOfN(n-1)

#print(sumOfN(int(input("Enter number to calculate >> "))))

def factorial(n):
    ''' Find factorial of a number '''
    if n in (0, 1): return 1
    return n * factorial(n-1)

#print(factorial(int(input("Enter number to calculate factorial >> "))))

def fibonacci(n):
    ''' Find the 'n'th term of fibonacci series '''
    if n in (0, 1) : return n
    return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(int(input("Which term of fibonacci series? >> "))))

def reverseString(string):
    ''' Reverse a string '''
    if len(string) == 1: return string
    return string[-1] + reverseString(string[:-1])

#print(reverseString(input("Enter a string >> ")))

def towerOfHanoi(num, src, dest, aux):
    ''' Tower of Hanoi [ I HAVEN'T PROPERLY UNDERSTOOD THIS YET ^_^ ] '''
    if num == 1: print("Moving the disk from", src, "to", dest)
    else:
        towerOfHanoi(num - 1, src, aux, dest)
        print("Moving the disk from", src, "to", dest)
        towerOfHanoi(num - 1, aux, dest, src)

#towerOfHanoi(int(input("Enter number of disks >> ")), 'A', 'C', 'B')
        
def binarySearch(lst, item, l = 0, h = False):
    ''' Binary Search '''
    if not h: h = len(lst)
    if l >= h: return False
    
    mid_index = l + (h - l) // 2
    if lst[mid_index] == item: return mid_index + 1
    elif item < lst[mid_index]: return binarySearch(lst, item, l, mid_index)
    else: return binarySearch(lst, item, mid_index, h)

#pos = binarySearch(list(eval(input("Enter comma seperated numbers >> "))),
#                   int(input("Enter item to search >> ")))

#if pos: print("Given item found at posititon", pos)
#else: print("Given item not found!")
    
