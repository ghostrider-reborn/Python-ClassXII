import itertools

"""
    Writing data in a text file
"""
def write_file(path, fname):
    f = open(path + "/" + fname, "a")
    write = "Y"
    while write.upper() == "Y":
        f.write(input("Enter line to write on the file >> ") + "\n")
        write = input("Enter Y to continue or N to end >> ")

#write_file(input("Enter directory of file >> "), input("Enter filename >> "))

"""
    File copier
"""
def file_opener(source, dest):
    try:
        source = open(source, "r")
        dest = open(dest, "a")
        for i in source.read():
            dest.write(i)
        
    except FileNotFoundError:
        print("Folder doesn't exist kiddo!")

#file_opener(input("Enter source path >> "), input("Enter destination path >> "))

"""
    Replace a character with another character in a text file
"""
def replace_char(path, char, replacement):
    try: f = open(path, "r+")
    except FileNotFoundError: return False
    
    while True:
        pos = f.tell()
        c = f.read(1)
        if not c: break
        if c == char:
            f.seek(pos)
            f.write(replacement)
    
    f.close()
    return True

#if replace_char(input("Enter path to the file >> "), input("Enter character to replace >> "), input("Enter replacement character >> ")): print("Success :-)")
#else: print("File doesn't exist! Check your path fool!")

def num_of_occurences(path,string):
    return open(path, "r").read().lower().count(string)

#print(num_of_occurences(input("Enter path to the text file >> "), input("Enter word to check number of its occurences >> ")))

"""
    Find number of words starting with letter 'E'
"""
def num_of_E(path):
    words = open(path, "r").read().split()
    num = 0
    for word in words:
        if word[0] == 'E': num += 1
    
    return num

#print(num_of_E(input("Enter path to the text file >> ")))

"""
    Find no. of lines and blank spaces in a file
"""
def num_lines_blank_spaces(path):
    content = open(path, "r").read()
    spaces = content.count(' ')
    lines = content.count('\n') + 1
    
    return (spaces, lines)

#result = num_lines_blank_spaces(input("Enter text file path >> "))
#print("There are", result[0], "spaces and", result[1], "lines")

"""
    Reverse the words starting with 't' in a text file
"""
def reverse_wds(path):
    for line in open(path, "r").readlines():
        words = line.split()
        for word in words:
            if word[0] in ("T", "t"): words[words.index(word)] = word[::-1]
        print(*words)

#reverse_wds("ok2.txt")
