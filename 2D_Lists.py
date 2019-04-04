"""
    2D LISTS
"""

def inputMatrix():
    ''' Input a matrix of a user entered rows and columns
        and return it as a 2D list '''
    rows = int(input("Enter no. of rows >> "))
    cols = int(input("Enter no. of columns >> "))
    return [[int(input("Enter element "+str(i+1)+" of row "+str(j+1)+" >> ")) for i in range(cols)] for j in range(rows)]

#rows = int(input("Enter no. of rows >> "))
#cols = int(input("Enter no. of columns >> "))
#matrix = inputMatrix(rows, cols)

def printMatrix(matrix):
    ''' Display a 2D matrix '''
    print()
    for i in matrix: print(*i)

def printDiagonalElements(matrix):
    ''' Print the main diagonal of a matrix '''
    assert all(len(matrix) == len(i) for i in matrix), "Only square matrix is allowed !!"
    print(*[matrix[i][i] for i in range(len(matrix))])

#printDiagonalElements(matrix)

def printLowerHalf(matrix):
    ''' Print the lower half of the matrix (including diagonal) '''
    assert all(len(matrix) == len(i) for i in matrix), "Only square matrix is allowed !!"
    for i in range(len(matrix)):
        print(*[matrix[i][j] for j in range(i+1)])

def printUpperHalf(matrix):
    ''' Print the upper half of the matrix (including diagonal) '''
    assert all(len(matrix) == len(i) for i in matrix), "Only square matrix is allowed !!"
    for i in range(len(matrix)):
        print('   '*i + str([matrix[i][j] for j in range(i, len(matrix))])[1:-1])

#printUpperHalf(matrix)

def addMatrix(m1, m2):
    ''' Add 2 matrices of the same size '''
    assert len(m1) == len(m2) and all(len(i) == len(j) for i in m1 for j in m2), "Size of both matrices should be same!"
    rows = len(m1)
    cols = len(m1[0])
    return [[m1[i][j] + m2[i][j] for j in range(cols)] for i in range(rows)]

'''rows = int(input("Enter no. of rows >> "))
cols = int(input("Enter no. of columns >> "))

print("\nMATRIX 1:\n")
m1 = inputMatrix(rows, cols)

print("\nMATRIX 2:\n")
m2 = inputMatrix(rows, cols)

added = addMatrix(m1, m2)
printMatrix(added)'''

def subtractMatrix(m1, m2):
    assert len(m1) == len(m2) and all(len(i) == len(j) for i in m1 for j in m2), "Size of both matrices should be same!"
    rows = len(m1)
    cols = len(m1[0])
    return [[m1[i][j] - m2[i][j] for j in range(cols)] for i in range(rows)]

'''rows = int(input("Enter no. of rows >> "))
cols = int(input("Enter no. of columns >> "))

print("\nMATRIX 1:\n")
m1 = inputMatrix(rows, cols)

print("\nMATRIX 2:\n")
m2 = inputMatrix(rows, cols)

subtracted = subtractMatrix(m1, m2)
printMatrix(subtracted)'''

def transposeMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]

matrix = inputMatrix()
printMatrix(matrix)
printMatrix(transposeMatrix(matrix))

