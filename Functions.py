"""
    FUNCTIONS EXERCISES
"""

def isArmstrong(num):
	''' Check if a number is an armstrong number, 
		without using inbuilt functions '''
    digs = Sum = 0
    t1_num = t2_num = num

    # Find number of digits
    while t1_num > 0:
        t1_num //= 10
        digs += 1

    # The main part
    while t2_num > 0:
        dig = t2_num % 10
        Sum += dig ** digs
        t2_num //= 10

    if Sum == num: return True
    return False

if isArmstrong(int(input("Enter a number >> "))): print("It is an amrstrong number")
else: print("It is not an amrstrong number")

def multiplyListElements(lst):
	''' Multiply all values in a list '''
    prod = 1
    for i in lst: prod *= i
    return prod

#print(multiplyListElements(list(eval(input("Enter numbers seperated by commas >> ")))))

def reverseString(string):
	''' Reverse a string '''
    rev_str = ""
    for i in string: rev_str = i + rev_str
    return rev_str

#print(reverseString(input("Enter a string > ")))

def numOfUpperLower(string):
	''' Number of uppercase and lowercase letters '''
    upper = lower = 0
    for i in string:
        if ord(i) in range(65,91): upper += 1
        elif ord(i) in range(97,123): lower += 1

    return (str(upper),str(lower))

#upper_lower = numOfUpperLower(input("Enter a string >> "))
#print("There are", upper_lower[0], "number of lowercase and", upper_lower[1], "number of uppercase characters")

def uniqueElementsOfList(lst):
	''' Find all unique elements in a list '''
    unique = []
	
    for i in lst:
        if i not in t_lst: unique.append(i)
    
    return unique

#print(uniqueElementsOfList(list(eval(input("Enter numbers seperated by commas >> ")))))

def evenNosOfList(lst):
	''' Find all even numbers in a list '''
    return [i for i in lst if i % 2 == 0]

#print("Even numbers in the list:", even_nos(list(eval(input("Enter numbers seperated by commas >> ")))))

def squaresTillN(n):
	''' Return a list of squares of numbers till 'n' '''
    return [i*i for i in range(1, n+1)]

#print(squaresTillN(int(input("Enter number till which squares should be generated >> "))))

def lettersAndDigits(string):
	''' Find number of letters and digits in a string '''
    ltrs = digs = 0
    
    for i in string:
        if i.isalpha(): ltrs += 1
        if i.isdecimal(): digs += 1

    return ltrs, digs

#ltr_digs = lettersAndDigits(input("Enter a string >> "))
#print("There are", ltr_digs[0], "letters and", ltr_digs[1], "digits in the string")

def sortHyphenSeperatedWords(string):
	''' parameter = a string of hyphen seperated words
		return = string of hyphen-seperated words sorted alphabetically '''
    words = string.split("-")

	# Bubble sort the words
    for i in range(len(words)):
        for j in range(len(words)-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]

    newstr = ""
    for i in words:
        newstr += i + '-'

    return newstr[:-1]

#print(sortHyphenSeperatedWords(input("Enter hyphen separated words >> ").lower()))

def frequencyOfLetters(sent):
	''' Find the frequency of every alphabets in a string '''
    freq = {}
    
    for ltr in sent:
        if ltr.isalpha():
            if ltr.upper() not in freq: freq[ltr.upper()] = 1
            else: freq[ltr.upper()] += 1

    return freq

#freq = frequencyOfLetters(input("Enter a sentence"))
#for i in freq: print("Frequency of letter", i, "=", freq[i])

def isBinsDivisibleBy5(string):
    return [i for i in string.split(",") if int(i, 2) % 5 == 0]

#print("The following binary numbers are divisible by 5:", *isBinsDivisibleBy5(input("Enter comma seperated binary numbers >> ")))

def isPrime(num):
    for i in range(2, num):
        if num % i == 0: return False
    
    return True

#if is_prime(int(input("Enter the number >> "))): print("The given number is a prime number")
#else: print("The given number is not a prime number")

def isPerfect(num):
    Sum = 0
    
    for i in range(1, num):
        if num % i == 0: Sum += i

    if Sum == num: return True
    return False

#if isPerfect(int(input("Enter a number > "))): print("It is a perfect number")
#else: print("It is not a perfect number")

def isPalindrome(num):
    orig_num = num
    rev_num = 0
    
    while num > 0:
        rev_num = rev_num * 10 + (num % 10)
        num //= 10

    if orig_num == rev_num: return True
    return False

#if isPalindrome(int(input("Enter a number >> "))): print("It is a palindrome number")
#else: print("It is not a palindrome number")

def factorial(num):
    if num in (0,1): return 1
	
	fac = 1
    for i in range(1, num): fac *= i
    return fac

#print("\nThe factorial of the number is", factorial(int(input("Enter a number > "))))