## Each Object has a Type
## Objects are : 
##         1.Scalar : int, float, bool
##         2.Non-Scalar: str
## Expressions: objects + operators
##         1. +, -, *, /(note), **, %
##         2. Parentheses
##         3. Comparison >, >=, <, <=, ==, !=
##         4. and, or, not a
## Type conversions
##         1. float(3) -- 3.0
##         2. int(3.9) -- 3
## Operations on Strings (Operator Overload)
##         1. 3 * 'a'
##         2. 'a' + 'b' 
##         3. 'a' + str(123)
##         4. len('abc)
## Extracting parts of strings
##        1. Indexing  'abc'[0], 'abc'[-1] - 'c'
##         2. Slicing   'abc'[1:3] - 'bc'
        
        
## Lect 2.5, slide 4
## Straight line program

x = 3
x = x*x
print(x)
y = float(raw_input('Enter a number:  '))
print (y*y)



## Branching Programs
## simplest branching statement: conditional: a test; a block; an optional block
## Lect 2.6, slide 2

x = int(raw_input('Enter an integer: '))
if x%2 ==0:
    print(' ')
    print('even')
else:
    print(' ')
    print('odd')
print('Done with conditional')



## Nested condionals

x = int(raw_input('Enter an integer: '))
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')
else:
    print('Not divisible by 2 and 3')
    
    
    
   
## Compound Booleans

x,y,z = 2,4,1
if x<y and x<z:
    print('x is the least')
elif y<z:
    print('y is least')
else:
    print('z is lease')
    
    
    
    
varA = 'kk'
varB =9
a = type(varA)
b = type(varB)
if a==str or b==str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    print('smaller')
