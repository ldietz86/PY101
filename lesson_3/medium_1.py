# Practice Problems: Medium 1
'''
Question 1:
Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens.

For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one 
more hyphen than the line above it. The output should start out like this:

-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
    ...
'''
string = "The Flintstones Rock!"

for i in range(1, 11):
   hyphen_str =  "-" * i
   print(f"{hyphen_str}{string}")

# Question 2: Fix the function below so it still works when the input is a negative number.
def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0: # This line checks if number is evenly divisible by divisor (if divisor is a factor of number).
            result.append(number // divisor)
        divisor -= 1
    return result

'''
Question 3:
Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. 
However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.
She wrote two implementations of the code for adding elements to the buffer.
What is the key difference between these implementations?
'''
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

'''
The key difference in add_to_rolling_buffer1 and add_to_rolling_buffer2 is how buffer is created.
add_to_rolling_buffer1 uses the append method, which performs in-place mutation, to add new_element to the end of buffer.
add_to_rolling_buffer2 reassigns buffer to the new list returned by concatenating buffer to [new_element].
'''

# Question 4: What will the following two lines of code output?
print(0.3 + 0.6) # 0.8999999999999999
print(0.3 + 0.6 == 0.9) # False

'''
use math.isclose() to compare floating-point numbers or the decimal module:
from decimal import Decimal
print(Decimal('0.3') + Decimal('0.6') == Decimal('0.9')) # True
'''
import math

print(0.3 + 0.6)
print(math.isclose(0.3 + 0.6, 0.9))

# Question 5: What do you think the following code will output?
nan_value = float("nan")

print(nan_value == float("nan"))

'''
nan -- not a number -- is a special numeric value that indicates that an operation that was intended to return a number failed. 
Python doesn't let you use == to determine whether a value is nan. You can use math.isnan() to test whether a value is nan:
'''
import math

nan_value = float("nan")

print(math.isnan(nan_value))

# Question 6: What is the output of the following code?
answer = 42

def mess_with_it(some_number):
    return some_number + 8 # new value is returned

new_answer = mess_with_it(answer)

print(answer - 8) # 34 -> answer references the integer 42

# Question 7: One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data.
# Did the family's data get ransacked? Why or why not?
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)

# Yes, Spot has increased everyone's age by 42 and changed everyone's gender to "other". 
# Dictionaries are mutable, so the item assignment and augmented assignment that take place inside the function both mutate the dictionary object.

# Question 8. Suppose we define a function named rps as follows, which follows the classic rules of the rock-paper-scissors game, 
# but with a slight twist: in the event of a tie, it just returns the choice made by both players.
def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"

print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock")) 
rps("rock", "paper") # => paper
rps("rock", "scissors") # => rock
rps("paper", "rock") # => paper
rps("paper", "rock") # => paper

# Question 9: What will the function invocation return?
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

bar(foo()) # False

# foo() returns "yes", ("yes" == "no") evaluates to False causing the and operator to short-circuit and return False

'''
Question 10:
In Python, every object has a unique identity that can be accessed using the id() function. This function returns the identity 
of an object, which is guaranteed to be unique for the object's lifetime. For certain basic immutable data types like short 
strings or integers, Python might reuse the memory address for objects with the same value. This is known as "interning".
Given the following code, predict the output:
'''
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c)) # True