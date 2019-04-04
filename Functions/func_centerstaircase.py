"""
    Pattern:
      *
     ***
    *****
"""

def pattern(rows):
    spaces = rows-1
    stars = 1
    
    while spaces>=0:
        print(spaces*' ' + stars*'*')
        spaces -= 1
        stars += 2

pattern(int(input("Enter no. of rows > ")))

