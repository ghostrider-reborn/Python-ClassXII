def separateOddEve(lst):
    ''' Seperates the odd and even numbers of a list such that
        even numbers are towards the left and odd towards right
        LIMITATIONS: 1) No use of inbuilt functions
                     2) No list splicing or generating new list
    '''
    for i in range(len(lst)-1):
        if lst[i] % 2 != 0:
            for j in range(i+1, len(lst)):
                if lst[j] % 2 == 0: lst[i], lst[j] = lst[j], lst[i]
    return lst

print(separateOddEve(list(eval(input("Enter list elements >> ")))))
            
