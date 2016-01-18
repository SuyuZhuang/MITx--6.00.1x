## Loop
##     range(n) = [0,1,2,3,...,n-1]
##     range(m,n) = [m,m+1,m+2,...,n-1]
    
## An example

x = 3
ans = 0
iterLeft =x
while (iterLeft != 0):
    ans = ans +x
    iterLeft = iterLeft -1
print (str(x)+'*'+str(x)+'='+str(ans))



## L3 Problem 2A
## a while loop.

i = 1
while i <6:
    print(i*2)
    i = i +1
print('Goodbye!')



## L3 Problem 2B
## a while loop.
print('Hello!')
i = 5
while i >0:
    print(i*2)
    i = i-1
    
    

## L3 Problem 2C
## Write a while loop that sums the values 1 through 'end'
end = 6
i = 1
sumn = 0
while i<end+1:
    sumn = sumn+i
    i=i+1
print sumn



## Floating point accuracy
num = 2
if num <0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num/2
if isNeg:
    result = '-' + result
print result




## Fractions

x = float(raw_input('Enter a decimal number between 0 and 1: '))
p = 0
while((2**p)*x)%1 != 0:
    print('Remainder = '+str((2**p)*x - int((2**p)*x)))
    p+=1
    print(p)

num = int(x*(2**p))

result = ''
if num == 0 :
    result = '0'
while num >0:
    result = str(num%2)+result
    num = num/2
    
for i in range(p - len(result)):
    result = '0'+result
    
print(result[-p])
result = result[0:-p]+'.'+result[-p:]  ## ?????
print('The binary representation of the decimal '+str(x)+' is '+str(result))




## Exhaustive enumeration
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while(abs(ans**2 - x))>=epsilon and ans <=x:
    ans += step
    numGuesses +=1
print('numGuesses = '+str(numGuesses))
if abs(ans**2 - x)>=epsilon:
    print('Failed on square root of '+str(x))
else:
    print(str(ans)+' is close to the square root of '+str(x))
  




## Bisection Search
## work well on problems with 'ordering' property
## Example of square root

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high+low)/2.0
while abs(ans**2 - x)>=epsilon:
    print('low = '+str(low)+'high = '+str(high)+'ans = '+str(ans))
    numGuesses += 1
    if ans**2 <x:
        low = ans
    else:
        high = ans
    ans = (low+high)/2.0
print('numGuesses = '+str(numGuesses))
print(str(ans)+' is close to square root of '+str(x))



### Printing on the same line
## Notice how if we have two print statements        
## print "Hi"
## print "there"
## The output will have each string on a separate line:
## Hi
## there
## Now try ading a comma after the print statement:
## print "Hi",
## print "there"
## The output will place the subsequent string on the same line:
## Hi there


## Secret Number

print("Please think of a number between 0 and 100!")
n = False
low = 0
high = 100
ans = 50

while (not n):
    print("Is your secret number %d?"%(ans))
    t = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if t!='h' and t!='l' and t!='c':
        print("Sorry, I did not understand your input.")
    elif t=='c':
        n = True
        print("Game over. Your secret number was: %d"%(ans))
        break
    elif t=='h':
        high = ans
        ans = (low+high)/2
    elif t=='l': 
        low = ans
        ans = (low+high)/2





  ## NEWTON-RAPHSON ROOT FINDING
 
epsilon = 0.01
y = 24.0
guess = y/2.0

while abs(guess*guess - y)>= epsilon:
    guess = guess-(((guess**2)-y)/(2*guess))
    print(guess)
print('Square root of '+str(y)+' is about '+str(guess))
        
