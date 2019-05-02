def hollowDiamond(size):
    ''' Generate a hollow diamond pattern made of stars
        [uses only one for loop]
        size - an odd integer specifying the number of rows '''
    assert size % 2 == 1, "Invalid size !!"
    space = ' '
    star = '*'
    for sp in range(size//2, -size//2, -1):
        sp = abs(sp)
        mid_sp = size - (sp + 1)*2
        if mid_sp <= 0: print(space*sp + star + space*sp)
        else: print(space*sp + star + space*mid_sp + star + space*sp)

hollowDiamond(int(input("Enter size of hollow diamond (odd no. of rows) >> ")))
