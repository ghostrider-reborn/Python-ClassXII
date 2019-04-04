#
# RECURSIVE FUNCTIONS
#

"""
    Recursive function for finding sum of first n natural nos
"""
def sumOfN(n, mode = "s"):
    mode = mode.lower()
    assert mode in ("s", "f"), "Mode can only be 's' or 'f' !!"
    modes = {"s": "+", "f": "*"}
    
    assert n >= 0, "Number shud be >= 0"
    if n == 0: return 0
    else: return eval("n"+modes[mode]+"sumOfN(n-1)")

#print(sumOfN(int(input("Enter number to calculate >> ")), input("Enter mode - 'f' for factorial or 's' for sum to n")))

"""
    Fibonacci series
"""
def fib(n):
    series = [0,1]
    index = 2
    assert n > 0, "Number of terms should be >= 1 !!"
    while len(series) <= n:
        series.append(series[index-1] + series[index-2])
        index += 1
    
    return series[:n]

#print("Fibonacci series:", fib(int(input("No. of terms (>= 1) >> "))))

"""
    Reverse a string
"""
def reverseString(string):
    if len(string) == 1: return string
    return string[-1] + reverseString(string[:-1])

#print(reverseString(input("Enter string >> ")))

"""
    Tower of Hanoi
"""
def towerOfHanoi(num, src, dest, aux):
    if num == 1: print("Moving the disk from", src, "to", dest)
    else:
        towerOfHanoi(num - 1, src, aux, dest)
        print("Moving the disk from", src, "to", dest)
        towerOfHanoi(num - 1, aux, dest, src)

towerOfHanoi(int(input("Enter number of disks >> ")), 'A', 'C', 'B')
        
    
