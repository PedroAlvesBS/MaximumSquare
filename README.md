# MaximumSquare
<p align="left">This project present two solutions for the same problem that it is: Given a matrix(M,N) boolean values representing a board of free (True) or occupied (False) fields. Find the size of the largest square of free fields.</p>

### Prerequisites
<p align="left">Before to get started you must install python(https://www.python.org/). The libraries used are all included in default installation.</p>

### Some instructions and examples
<p align="left">Getting started with the code. Using some text editor (i.e. https://notepad-plus-plus.org/), you must choose the way your binary matrix 
 will be generated, if manualy or automatic. The default way is to insert manually, if you want to change this, you must to comment the snippet:</p>


```
 #Manual Matrix
 matrix =   [           
                [1,1,0,1,1,1],
                [1,1,0,1,1,1],
                [1,1,0,1,1,1],
           ]
 
find_sqr(matrix)
```
<p>and remove the comment mark (''') on:</p>

```
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
```


<p>In automatic mode you will be asked for the number of rows and the number o columns, different from manual. In manual the number of columns must 
be the same or the execution will break, so take care using manual mode and pay atention to the numbers of columns used.</p>

<p align="left">Inside the folder that cointains both files. For running the brute force solution. Using terminal type:</p>

```
python3 bruteforce.py
```

<p>And for running the dynamic solution for the problem, type:</p>

```
python3 dynamicprog.py
```

<p>After running the code, the answer for the initial question will be displayed.</p>
