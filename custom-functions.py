def reverse_string(string):
    ''' Reverse a string '''
    rev_str = ""
    for i in string: rev_str = i + rev_str
    return rev_str

def factorial(n):
    ''' Find factorial of a number '''
    if n in (0, 1): return 1
    return n * factorial(n-1)

def fibonacci_term(n):
    ''' Find the 'n'th term of fibonacci series '''
    if n in (0, 1) : return n
    return fibonacci_term(n-1) + fibonacci_term(n-2)

def fibonacci(n):
    ''' Return the fibonacci series upto nth term in a list '''
    return [fibonacci_term(i) for i in range(0, n+1)]
