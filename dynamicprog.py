from os import system
system('clear')

def find_sqr(matrix):
    n_rows,n_columns = len(matrix),len(matrix[0])
    
    if(matrix == None or n_rows == 0 ):
        return 0

    aux_mat = [[0 for j in range(n_columns)] for i in range(n_rows)]

    max_ones_lenght = 0

    for row in range(n_rows):
        for column in range(n_columns):
            aux_mat[row][column] = matrix[row][column]

            if (row > 0 and column > 1 and matrix[row][column] == 1):
                aux_mat[row][column] = 1 + min(aux_mat[row][column-1], aux_mat[row-1][column], aux_mat[row-1][column-1])
            if max_ones_lenght < aux_mat[row][column]:
                max_ones_lenght = aux_mat[row][column]
    print(f'\nThe size of the largest square is: {max_ones_lenght}\n')

#Manual Matrix
matrix =   [           
            
                [1,1,0,1,1,1],
                [1,1,0,1,1,1],
                [1,1,0,1,1,1],
           ]

find_sqr(matrix)

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
    matrix = [[randint(0,1) for j in range(column)] for i in range(row)]
    for i in range(row):
        print(f'{matrix[i]}\n')
    return matrix

matrix = mat_bin_gen()
find_sqr(matrix)    
'''