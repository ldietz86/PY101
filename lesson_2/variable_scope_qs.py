# 24. Variable Scope Exercises

# Q1. What will the following code print and why?
num = 5

def my_func():
    print(num)

my_func()

'''
This code will print 5. num on line 4 is the same as num on line 1. 
num on line 1 is initialized in the global scope making it accessible 
from inside my_func.
'''

# Q2. What will the following code print and why?
num = 5

def my_func():
    num = 10

my_func()
print(num)

'''
This code will print 5. num initialized inside my_func creates a local 
variable with function scope. When num is passed to print on line 7, 
Python uses the global num variable.
'''

# Q3. What will the following code print and why?
num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

'''
This code will print 10. The global statement is being used inside my_func 
which tells Python to look to the global scope for the variable that will 
be reassigned. Assignments to num inside my_func should affect the num in
the global scope ∴ num = 10 is reassigning the global num variable. 
'''

# Q4. What will the following code print and why? 
def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

'''
This code will print Hello World. outer_var is initialized inside the outer
function giving it function scope. That makes outer_var accessible inside
that function and any nested functions. The inner function can access variables
from its enclosing outer scopes.
'''

# Q5. What will the following code do?
def my_func():
    num = 10

my_func()
print(num)

'''
This code will raise a NameError. num is initialized inside my_func which creates
a local variable num with function scope. It is not accessible from outside the 
function.
'''

# Q6. What will the following code print and why?
def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

'''
This code will print Inner 1: 25 and Inner2: 15. A variable x is initialized inside 
my_func and references 15. Another variable x is initialized inside inner_func1 and 
references 25. inner_func1 prints its local x value. inner_func2 does not have access 
to x inside inner_func1, so it prints the x in my_func (the nearest enclosing scope).
'''