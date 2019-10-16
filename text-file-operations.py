"""
    FILE HANDLING
"""

import os

def writeToFile(path):
    ''' Write to a file and create one if doesn't exist '''
    if os.path.isfile(path): 
        if input("File does not exist. Create new file? (Y/N) >> ").upper() == 'Y': f = open(path ,"w")

    with open(path, "a") as f:
        write = "Y"
        while write.upper() == "Y":
            f.write("\n" + input("Enter line to write on the file >> "))
            write = input("DO you want to add another line ? (Y/N) >> ")

#write_file(input("Enter directory of file >> "), input("Enter filename >> "))

def fileCopier(source, dest):
    ''' Copy contents of a file to another file '''
    assert os.path.isfile(source), "Source file does not exist !!"
    with open(source, "r") as f_src, open(dest, "w") as f_dest:
        f_dest.write(f_src.read())
        

#fileCopier(input("Enter source path >> "), input("Enter destination path >> "))

def replaceCharInFile(path, char, replacement):
    ''' Replace a given character in a text file '''
    assert os.path.isfile(path), "Path does not exist !!"

    with open(path, "r+") as f:
        found = False
        while True:
            pos = f.tell()
            c = f.read(1)
            if not c: break
            if c == char:
                f.seek(pos)
                f.write(replacement)
                found = True

    return found

#replaceCharInFile(input("Enter path to the file >> "), input("Enter character to replace >> "), input("Enter replacement character >> "))

def numOfOccurances(path,string):
    ''' Find the number of occurances of a string in a text file '''
    return open(path, "r").read().lower().count(string)

#print(numOfOccurances(input("Enter path to the text file >> "), input("Enter word to check number of its occurences >> ")))

def numOfWordsStartingWith(path, char):
    ''' Find the number of words starting with a specified
        letter, in a text file '''
    assert os.path.isfile(path), "Path does not exist !!"

    with open(path, "r") as f:  
        return sum([i for i in f.read().split() if i[0] == char])

#print(num_of_E(input("Enter path to the text file >> ")))

def numOfLinesAndSpaces(path):
    ''' Find the number of spaces and newlines in a text file '''
    assert os.path.isfile(path), "Path does not exist !!"

    with open(path, "r") as f:
        spaces = f.read().count(' ')
        lines = f.read().count('\n') + 1
    
    return (spaces, lines)

#result = numOfLinesAndSpaces(input("Enter text file path >> "))
#print("There are", result[0], "spaces and", result[1], "lines")

def reverseWordsStartingWith(path, char):
    ''' Reverse the words starting with a specified character
        in a text file '''
    with open(path, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if word[0].upper() == char.upper(): words[words.index(word)] = word[::-1]
            print(*words)

#reverseWordsStartingWith("ok2.txt")
