"""
    BINARY FILE DUMPING
    USING pickle MODULE
"""
import pickle, os

def writeBinary(path, obj, mode = "W"):
    """ Write an object to a binary file
        mode: "A" for append, "W" for create/overwrite (default) """
    
    mode = mode.upper()
    modes = {"W": "wb", "A": "ab"}
    
    if os.path.isfile(path) and mode == "W":
        if input("Specified file already exists! Overwrite? (Y/N) >> ").lower() != "y": return None
    
    with open(path, modes[mode]) as file:
        pickle.dump(obj, file)

    print("\nBinary file created at", os.path.realpath(path))

def readBinary(path):
    with open(path, "rb") as file:
        while True:
            try: pickle.load(file)
            except EOFError: pass

#def modifyRecord(path, roll_num):
#    with open(path, "wb+") as file:

#testList = [input("Enter naem of the stedunt >> "), int(input("Enter the roll nomber of the stedunt >> ")), int(input("Enter the failure marks of tha stedunt >> "))]
#path = input("Enter path of the binarie file (extension .dat default) >> ") + ".dat"

#writeBinary(path, testList)
#print("\nBinary file output:", readBinary(path))

def binarySearch(lst, key):
    found = False
    h = len(lst)
    l = 0
    while not found and l <= h:
        mid_index = (h-l // 2) - 1
        if lst[mid_index] == key:
            found = True
            return mid_index
        elif lst[mid_index] < key: h = mid_index
        else: l = mid_index
    
    return found

def recBinarySearch(lst, key, h, l = 0):
    
    pos = (h-l // 2) - 1
    mid_ele = lst[pos]
    
    if h < l: return False
    
    if mid_ele == key: return pos
    elif mid_ele < key: recBinarySearch(lst, key, pos)
    else: recBinarySearch(lst, key, h, pos)

recBinarySearch([1,2,3,4,5,6,7,8,9], 5)
    
    
