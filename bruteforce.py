from os import system
system('clear')

def find_sqr(mat):
    n_rows,n_columns = len(mat),len(mat[0])
    
    if(mat == None or n_rows == 0 ):
        return 0

    max_ones_lenght = 0

    for row in range(n_rows):
        for column in range(n_columns):
            if (mat[row][column] == 1):
                sqrlen = 1
                thereIsSquare = True
                while ((sqrlen + row < n_rows) and (sqrlen + column < n_columns) and (thereIsSquare) ):
                    for i in range(column, sqrlen + column +1 ):
                        if (mat[row+sqrlen][i] == 0):
                            thereIsSquare=False
                            break
                    for i in range(row, sqrlen + row +1 ):
                        if (mat[i][column+sqrlen] == 0):
                            thereIsSquare=False
                            break
                    if (thereIsSquare):
                        sqrlen+=1
                if (max_ones_lenght < sqrlen):
                    max_ones_lenght=sqrlen
    print(f'\nThe size of the largest square is: {max_ones_lenght}\n')

#Manual Matrix
mat =   [
           [1,1,0,1,1,1],
           [1,1,0,1,1,1],
           [1,1,0,1,1,1],
        ]

find_sqr(mat)

#Automatic Matrix
'''
def int_validation(string_name):
    from os import system
    from time import sleep
    number = None
    while True:
        try:
            number = int(input(f'Please insert an integer number greater than "0" for {string_name}\n>'))
            if number < 1:
            	raise
        except:
            print('\nInvalid Number...')
            sleep(2)
            system('clear')
        else:
            sleep(1)
            system('clear')
            break
    return number

def mat_bin_gen():
    from random import randint
    row = int_validation('rows')
    column = int_validation('columns')
    mat = [[randint(0,1) for j in range(column)] for i in range(row)]
    for i in range(row):
        print(f'{mat[i]}\n')
    return mat

matrix = mat_bin_gen()
find_sqr(matrix)    
'''