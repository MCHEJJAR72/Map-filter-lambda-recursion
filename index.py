
Tasks Today:
Lambda Functions
     a) Syntax
     b) Saving to a Variable
     c) Multiple Inputs
     d) Passing a Lambda into a Function
     e) Returning a Lambda from a Function
     f) In-Class Exercise #1
Map
     a) Syntax
     b) Using Lambda's with Map
     c) In-Class Exercise #2
Filter
     a) Syntax
     b) Using Lambda's with Filter
     c) In-Class Exercise #3
Reduce
     a) Syntax
     b) Using Lambda's with Reduce
     c) In-Class Exercise #4
Recursion
     a) Implementing a Base
     b) Writing a Factorial Function
     c) In-Class Exercise #5
Generators & Iterators
     a) Yield Keyword
     b) Inifinite Generator
     c) In-Class Exercise #6
Exercises
     a) Exercise #1 - Filtering Empty Strings
     b) Exercise #2 - Sorting with Last Name
     c) Exercise #3 - Conversion to Farhenheit
     d) Exercise #4 - Fibonacci Sequence
Lambda Functions
Lambda functions... or "Anonymous Functions" are referring to inline functions with no name. The keyword lambda denotes the no name function, and executes within a single line. Without saving it to a variable; however, it is not able to be used, unless passed in either as a paramater or within list comprehension.
Written as "(keyword lambda) (one or more inputs) (colon) (function to be executed)"

Syntax
def addTwo(x):
    return x + 2

print(addTwo(4))

# The lambda version..
# Without using a variable to pass in data
print((lambda x: x +2)(4))

# Using a variable 
a_num = 4
print((lambda x: x +2)(a_num))
6
6
6
Saving to a Variable
f_test = lambda x: x + 2

f_test(4)
6
Multiple Inputs
# Multiple inputs with no variable
print((lambda x, y, z: x * y * z)(3, 5, 8))

# Multiple inputs with a variable attached
x_test = lambda x, y, z: x * y * z
print(x_test(3, 5, 8))
120
120
Passing a Lambda into a Function
def multiply(f, num):
    """
        f expects a lambda function
        num expects a number
    
    """
    return f(num)

multiply(lambda x: x * x, 4)
Returning a Lambda from a Function
# Regular defined function
def multiply_test(num):
    return num * 4

# Function within a function:
def returnFunc():
    test = 4
    def multiply(num):
        return num * 2
    return multiply

f_return = returnFunc()
print(returnFunc())
print(f_return(4))

# Lambda function returned from a regular function
def returnLam(b,c):
    return lambda x, a: x + a + b + c
r_lamb = returnLam(4,5)
print(r_lamb(5,5))
<function returnFunc.<locals>.multiply at 0x7fe3b68af0d0>
8
19
If Statements within Lambdas
# Lambda x: True if (condition) else False
f_condtion = lambda num: num * 2 if num > 10 else num + 2

print(f_condtion(8))
print(f_condtion(12))
print(f_condtion(10))
10
24
12
In-Class Exercise #1
Write an anonymous function that cubes the arguments passed in and assign the anonymous function to a variable 'f'.

f = lambda x: x**2

f(3)
9
Map
The map function allows you to iterate over an entire list while running a function on each item of the list. This is why the map function works well with lambda's, because it simplifies things and you write less lines of code.
The syntax for a map function is "map(function to be used, list to be used)"
However, you must be careful, as the map function returns a map object, not a list. To turn it into a list we use the list() type conversion.

Syntax
#map(func, iterable)
# An iterable has to be something like a list, dict, tuple, set
# Normally the usage of map happens with a pre-defined function - but we can use lambdas as well

def squared(num,num2):
    if num < 10 and num2 < 10:
        return num ** 2, num2 **2
    else:
        return num, num2
        
numbers = [4, 11, 20, 3, 15, 20]
more_nums = [4, 10, 3, 2, 6]
        
squared_nums_map = list(map(squared, numbers, more_nums))
print(squared_nums_map)
[(16, 16), (11, 10), (20, 3), (9, 4), (15, 6)]
Using Lambda's with Map
# map(lambda x: do something, iterable)
# Using lambda in map happens inline or on one line
# list(map(lambda x: x * 2, nums))
squared_nums_lambda = list(map(lambda x, y:(x ** 2, y ** 2) if x < 10 and y < 10 else (x,y), numbers, more_nums))
print(squared_nums_lambda)
[(16, 16), (11, 10), (20, 3), (9, 4), (15, 6)]
In-Class Exercise #2
Use the map function to double each number and minus it by one in the list by using a lambda function

nums = [4, 11, 6, 3, 8]
more_nums = [4, 7, 15, 4, 11]

double_num = list(map(lambda x, y:(x*2-1, y*2-1), nums, more_nums))
print(double_num)
[(7, 7), (21, 13), (11, 29), (5, 7), (15, 21)]
Filter()
Filter's are similar to the map function, where you're able to pass a function argument and a list argument and filter out something from the list based on the conditions passed. Similar to the map function, it returns a filter object, so you need to type convert it to a list()

Syntax
names = ['Bob', 'Andy', 'Max', 'Evan', 'Angelica']

def a_names(name):
    if name[0].lower() == 'a':
        return True
    else: 
        return False
new_names_list = list(filter(a_names, names))
print(new_names_list)
['Andy', 'Angelica']
Using Lambda's with Filter()
new_names_lambda = list(filter(lambda name: True if name[0].lower() == 'a' else False, names))
print(new_names_lambda)
['Andy', 'Angelica']
In-Class Exercise #3
Filter out all the numbers that are below the mean of the list.
Hint: Import the 'statistics' module

from statistics import mean

nums = [4, 7, 15, 4, 11]

new_nums_lambda = list(filter(lambda num: True if num <= mean(nums) else False, nums))
print(new_nums_lambda)
[4, 7, 4]
Reduce()
Be very careful when using this function, as of Python 3 it's been moved to the 'functools' library and no longer is a built-in function.
The creator of Python himself, says to just use a for loop instead.

Syntax
from functools import reduce 

# reduce(function, iterable)

list_1 = [2, 4, 6, 8, 10]

def addNums(num1, num2):
    return num1 + num2

result_add = reduce(addNums, list_1)

print(result_add)

# Subtraction a list of numbers
def subtractNums(num1, num2):
    return num1 - num2

result_sub = reduce(subtractNums, list_1)
print(result_sub)
30
-26
Using Lambda's with Reduce()
result_lamb = reduce(lambda x, y: x + y, list_1)
print(result_lamb)
-26
In-Class Exercise #4
Use the reduce function to multiply the numbers in the list below together with a lambda function.

my_list = [1, 2, 3, 4]
multiply_lamb = reduce(lambda x, y: x*y, my_list)
print(multiply_lamb)
24
Recursion
Recursion means that a function is calling itself, so it contanstly executes until a base case is reached. It will then push the returning values back up the chain until the function is complete. A prime example of recursion is computing factorials... such that 5! (factorial) is 5*4*3*2*1 which equals 120.

Implementing a Base Case
def addNums(num):
    #Here is our base case..
    if num <= 1:
        print('addNums(1) = 1')
        return num 
    else:
        print(f'addNums({num}) = {num} + addNums({num - 1})')
        return num + addNums(num - 1)
addNums(5)
addNums(5) = 5 + addNums(4)
addNums(4) = 4 + addNums(3)
addNums(3) = 3 + addNums(2)
addNums(2) = 2 + addNums(1)
addNums(1) = 1
15
Writing a Factorial Function
# 5! = 5 * 4 * 3 * 2 * 1
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)
factorial(5)
120
In-Class Exercise #5
Write a recursive function that subtracts all numbers to the argument given.

# Return num - subNums(num - 1)
# subNums(10)

def subNums(num):
    if num <=1:
        return 1
    else:
        return num - subNums(num-1)
    
subNums(10)
5
Generators
Generators are a type of iterable, like lists or tuples. They do not allow indexing, but they can still be iterated through with for loops. They are created using functions and the yield statement.

Yield Keyword
The yield keyword denotes a generator, it doesn't return so it won't leave the function and reset all variables in the function scope, instead it yields the number back to the caller.

def my_range(stop, start, step = 2):
    while start < stop:
        yield start #yield keyword denotes a generator
        start += step
for i in my_range(20, start = 2):
    my_generator_value = i
    print(my_generator_value)
    
my_range(20, start = 2)
2
4
6
8
10
12
14
16
18
<generator object my_range at 0x7fe3b7779e40>
Infinite Generator
# bad, never create infinite loops
In-Class Exercise #6
Create a generator that takes a number argument and yields that number squared, then prints each number squared until zero is reached.

def m_squared(start, stop = 0, step = 1):
    while start >= stop:
        yield start**2
        start -= step
for i in m_squared(10):
    print(i)
    100
81
64
49
36
25
16
9
4
1
0
Exercises
Exercise #1
Filter out all of the empty strings from the list below

Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def f_places(place):
    if place == "":
        return False
    elif place[0] == " ":
        return False
    else:
        return True

new_places = list(filter(f_places, places))
print(new_places)
['Argentina', 'San Diego', 'Boston', 'New York']
Exercise #2
Write an anonymous function that sorts this list by the last name...
Hint: Use the ".sort()" method and access the key"

Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key = lambda x: x.upper().split()[-1])
print(author)
['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']
Exercise #3
Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)] 

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

celsius_to_fah =list(map(lambda x: (x[0], (9/5)*x[1] + 32), places))
print(celsius_to_fah)
[('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
Exercise #4
Write a recursion function to perform the fibonacci sequence up to the number passed in.

Output for fib(5) =>  Iteration 0: 1 Iteration 1: 1 Iteration 2: 2 Iteration 3: 3 Iteration 4: 5 Iteration 5: 8

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-1) + fib(n-2)
for n in range(0,6):
    print('Iteration',n, ":", fib(n))
Iteration 0 : 1
Iteration 1 : 1
Iteration 2 : 2
Iteration 3 : 3
Iteration 4 : 5
Iteration 5 : 8