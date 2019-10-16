"""
    2D LISTS (MATRICES)
"""

def checkMatrix(m1, m2, square = False):
    ''' Check if the size (rows & cols) of 2 matrices are same
        Additional optional parameter: square - Check if both are square matrices too '''
    if square: return all(len(m1) == len(m2) == len(i) == len(j) for i in m1 for j in m2)
    return (len(m1) == len(m2) and all(len(i) == len(j) for i in m1 for j in m2))

def isSquareMatrix(matrix):
    ''' Check if a matrix is a square matrix '''
    return all(len(matrix) == len(i) for i in matrix)

def inputMatrix():
    ''' Input a matrix of a user entered rows and columns
        and return it as a 2D list '''
    rows = int(input("ENTER NO. OF ROWS >> "))
    cols = int(input("ENTER NO. OF COLUMNS >> "))
    return [[int(input("Enter element "+str(i+1)+" of row "+str(j+1)+" >> ")) for i in range(cols)] for j in range(rows)]

def printMatrix(matrix):
    ''' Display a matrix
        TODO: Print in a decently formatted manner '''
    print()
    for i in matrix: print(*i)
    

def printDiagonalElements(matrix):
    ''' Print the main diagonal of a matrix '''
    assert isSquareMatrix(matrix), "Only square matrix is allowed!"
    print(*[matrix[i][i] for i in range(len(matrix))])


def printLowerHalf(matrix):
    ''' Print the lower half of the matrix (including diagonal) '''
    assert isSquareMatrix(matrix), "Only square matrix is allowed!"
    for i in range(len(matrix)):
        print(*[matrix[i][j] for j in range(i+1)])

def printUpperHalf(matrix):
    ''' Print the upper half of the matrix (including diagonal) '''
    assert isSquareMatrix(matrix), "Only square matrix is allowed!"
    for i in range(len(matrix)):
        print(*[matrix[i][j] for j in range(i, len(matrix))])

def addMatrix(m1, m2):
    ''' Add 2 matrices of the same size '''
    assert checkMatrix(m1, m2), "Size of both matrices should be same!"
    rows = len(m1)
    cols = len(m1[0])
    return [[m1[i][j] + m2[i][j] for j in range(cols)] for i in range(rows)]

'''print("\nMATRIX 1:\n")
m1 = inputMatrix()

print("\nMATRIX 2:\n")
m2 = inputMatrix()

added = addMatrix(m1, m2)
printMatrix(added)'''

def subtractMatrix(m1, m2):
    ''' Subtract 2 matrices '''
    assert checkMatrix(m1, m2), "Size of both matrices should be same!"
    rows = len(m1)
    cols = len(m1[0])
    return [[m1[i][j] - m2[i][j] for j in range(cols)] for i in range(rows)]

'''print("\nMATRIX 1:\n")
m1 = inputMatrix()

print("\nMATRIX 2:\n")
m2 = inputMatrix()

subtracted = subtractMatrix(m1, m2)
printMatrix(subtracted)'''

def transposeMatrix(matrix):
    ''' Transpose a matrix '''
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]

#matrix = inputMatrix()
#printMatrix(matrix)
#printMatrix(transposeMatrix(matrix))

def multiplyMatrix(m1, m2):
    ''' Multiply 2 matrices '''
    m2 = transposeMatrix(m2)
    assert checkMatrix(m1, m2), "Invalid matrices!"
    rows = len(m1)
    cols = len(m2)
    return [[sum(m1[i][k] * m2[j][k] for k in range(cols)) for j in range(rows)] for i in range(rows)]

'''print("\nMATRIX 1:\n")
m1 = inputMatrix()

print("\nMATRIX 2:\n")
m2 = inputMatrix()

mult = multiplyMatrix(m1, m2)
printMatrix(mult)'''
