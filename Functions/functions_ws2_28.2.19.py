"""
    FUNCTIONS EXERCISES
"""


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

#print("The number", is_armstrong(int(input("Enter the number > "))), "armstong number")

"""
    Function to multiple all values in a list
"""
def list_multiply(lst):
    prod = 1
    for i in lst: prod *= i
    return prod

#print(list_multiply(list(eval(input("Enter numbers seperated by commas > ")))))

"""
    Function to reverse a string
"""
def reverse_str(string):
    rev_str = ""
    for i in string: rev_str = i + rev_str
    return rev_str

#print(reverse_str(input("Enter a string > ")))
"""
    Function to calculate number of upper & lowercase chars in a str
"""
def upper_lower_str(string):
    upper = lower = 0
    for i in string:
        if ord(i) in range(65,91): upper += 1
        elif ord(i) in range(97,123): lower += 1

    return (str(upper),str(lower))

#upper_lower = upper_lower_str(input("Enter a string > "))
#print("There are", upper_lower[0], "number of lowercase and", upper_lower[1], "number of uppercase characters")

"""
    Return a list containing unique elements of given list
"""
def unique_lst(lst):
    t_lst = []
    for i in lst:
        if i not in t_lst: t_lst.append(i)
    
    return t_lst

#print(unique_lst(list(eval(input("Enter numbers seperated by commas > ")))))

"""
    Return all even numbers of a list
"""
def even_nos(lst):
    even = [i for i in lst if i % 2 == 0]
    return even

print("Even numbers in the list:", even_nos(list(eval(input("Enter numbers seperated by commas > ")))))

"""
    Return a list of squares of the given list
"""
def squares_till_num(num):
    sq = []
    for i in range(1, num+1): sq.append(i**2)
    return sq

#print(squares_till_num(int(input("Enter number till which squares should be generated > "))))

"""
    To find number of letters & digits in a string
"""
def ltrs_digs(string):
    ltrs = 0
    digs = 0
    
    for i in string:
        if i.isalpha(): ltrs += 1
        if i.isdecimal(): digs += 1

    return ltrs, digs

#ltr_dig = ltrs_digs(input("Enter a string > "))
#print("There are", ltr_dig[0], "letters and", ltr_dig[1], "digits in the string")

"""
    Parameter: string of hyphen-seperated words
    Return value: string of hyphen-seperated words sorted alphabetically
"""
def hyphen_words_sort(string):
    words = string.split("-")

    for i in range(len(words)):
        for j in range(0, len(words)-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]

    newstr = ""
    for i in words:
        newstr += i + '-'

    return newstr[:-1]

#print(hyphen_words_sort(input("Enter hyphen separated words > ").lower()))

"""
    Compute frequency of each letter in a sentence
"""
def freq_letters(sent):
    freq = {}
    
    for ltr in sent:
        if ltr.isalpha():
            if ltr.upper() not in freq: freq[ltr.upper()] = 1
            else: freq[ltr.upper()] += 1

    return freq

#freq = freq_letters(input("Enter a sentence"))
#for i in freq: print("Frequency of letter", i, "=", freq[i])

"""
    Dict having keys as nos between 1 to 20 and the corresponding values as squares
"""
def cust_dict():
    dic = {}
    for i in range(1, 21): dic[i] = i*i
    for i in dic: print(dic[i])

#cust_dict()

"""
    From a list find the binary numbers that are divisible by 5
"""
def bin_div_by_5(string):
    bins = string.split(",")
    return [i for i in bins if int(i, 2) % 5 == 0]

div_by_5 = bin_div_by_5(input("Enter comma seperated binary numbers > "))
print("The following binary numbers are divisible by 5:", *div_by_5)
