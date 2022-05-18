action = input('To perform additon enter add, for subtraction enter subtract\n'\
        'for division enter divide, for multiplication enter multiply\n'\
        'and for modulus enter mod: ')
        
if action not in ['add', 'subtract', 'multiply', 'divide', 'mod']:
    exit('Operation not recognised')

n1 = input('First number: ')
n2 = input('Second number: ')

def add(n1, n2):
    try:
        print('{} + {} = {:.4f}'.format(n1, n2, float(n1) + float(n2)))
    except:
        print('Enter number only')

def subtract(n1, n2):
    try:
        print('{} - {} = {:.4f}'.format(n1, n2, float(n1) - float(n2)))
    except:
        print('Enter number only')

def divide(n1, n2):
    try:
        print('{} / {} = {:.4f}'.format(n1, n2, float(n1) / float(n2)))
    except:
        print('Enter number only')

def multiply(n1, n2):
    try:
        print('{} * {} = {:.4f}'.format(n1, n2, float(n1) * float(n2)))
    except:
        print('Enter number only')

def mod(n1, n2):
    try:
        print('{} % {} = {}'.format(n1, n2, int(n1) % int(n2)))
    except:
        print('Enter number only')

if (action == 'add'):
    add(n1, n2)
elif (action == 'subtract'):
    subtract(n1, n2)
elif (action == 'divide'):
    divide(n1, n2)
elif (action == 'multiply'):
    multiply(n1, n2)
elif (action == 'mod'):
    mod(n1, n2)
else:
    print('Input not recognised')


