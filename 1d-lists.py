"""
    1D List operations
"""

def linearSearch(lst, item):
    ''' Linear Search '''
    for i in range(0, len(lst)):
        if lst[i] == item: return i+1
    
    return False

#pos = linearSearch(list(eval(input("Enter list as comma seperated numbers >> "))),
#                   int(input("Enter element to search >> ")))

#if search: print("Found given element at position", search)
#else: print("Element", item, "not found")

def binarySearch(lst, item):
    ''' Binary Search '''
    lower = 0
    upper = len(lst)
    
    while lower < upper:
        mid_ele = (lower + upper) // 2
        if lst[mid_ele] == item: return mid_ele + 1
        elif lst[mid_ele] > item: upper = mid_ele
        else: lower = mid_ele

    return False
        
#pos = binarySearch(list(eval(input("Enter comma seperated numbers >> "))),
#                   int(input("Enter item to search >> ")))

#if pos: print("Found given element at position",  pos)
#else: print("Given item not found!")

def bubbleSort(lst):
    ''' Bubble Sort '''
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]: lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

#lst = list(eval(input('Enter comma separated numbers >> ')))
#print("Sorted:", bubbleSort(lst))

def insertElement(lst, element, pos):
    ''' Insert a given element in a given list at a given posititon, in-place '''
    lst += [0]
    index = pos-1
    
    for i in range(len(lst)-1, index, -1): lst[i] = lst[i-1]
    
    lst[index] = element
    
    return lst
        
#print(insertElement(list(eval(input("Enter comma seperated numbers (list) >> "))),
#                    int(input("Enter the element to insert >> ")),
#                    int(input("Enter the position >> "))))

def insertElementSorted(lst, element):
    ''' Insert a number in a sorted list in its correct posititon
        so that the list still remains sorted, in-place '''
    
    if element <= lst[0]: index = 0
    elif element >= lst[-1]: index = len(lst)
    else:
        for i in range(1, len(lst) - 1):
            if element >= lst[i-1] and element <= lst[i]: index = i

    return insertElement(lst, element, index + 1)
        
#print(insertElementSorted(list(eval(input("Enter sorted comma seperated numbers (list) >> "))),
#                          int(input("Enter the element to insert >> "))))

def deleteElement(lst, element):
    ''' Delete a given element from a list, in-place '''
    pos = linearSearch(lst, element)
    if not pos: return "Specified element does not exist in the given list !"
    
    for i in range(pos-1, len(lst)-1):
        lst[i] = lst[i+1]

    return lst[:-1]

#print(deleteElement(list(eval(input("Enter a list of numbers, comma-separated >> "))),
#                    int(input("Enter element if you want do delete >> "))))

def selectionSort(lst):
    ''' SELECTION SORT '''
    for i in range(len(lst)):
        smallest = i
        for j in range(i+1, len(lst)):
            if lst[j] <= lst[smallest]: smallest = j
        
        lst[i], lst[smallest] = lst[smallest], lst[i]

    return lst

#print("Sorted:", selectionSort(list(eval(input('Enter comma separated numbers >> ')))))

def swapHalfList(lst):
    ''' Swap 1st and 2nd half parts of a given list '''
    assert len(lst) % 2 == 0, "List should have even number of elements!"

    for i in range(len(lst)//2):
        lst[i], lst[len(lst)//2 + i] = lst[len(lst)//2 + i], lst[i]

    return lst

#print(swapHalfList(list(eval(input("Enter list as comma-seperated numbers >> ")))))
