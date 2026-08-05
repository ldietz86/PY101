# Practice Problems: Hard 1
# Question 1: Will the following functions return the same results?
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

'''
first() returns a dictionary with the key 'prop1' and value "hi there"
second() returns None because the return statement on line 9 exits out of the function
The dictionary definition on line 10 is treated as unreachable code that is never executed
'''

# Question 2: What does the last line in the following code output?
dictionary = {'first': [1]}
num_list = dictionary['first'] # references the original list in dictionary
num_list.append(2) # append performs in-place mutation ∴ the original list becomes [1, 2]

print(num_list) # [1, 2]
print(dictionary) # {'first': [1, 2]}


# To modify num_list but not dictionary, we can initialize num_list with a reference to a copy of the original list: 
dictionary = {"first": [1]}
num_list = dictionary["first"].copy()
num_list.append(2)

# or we can use list slicing which returns a new list:
dictionary = {"first": [1]}
num_list = dictionary["first"][:]
num_list.append(2)

# Question 3: Given the following similar sets of code, what will each code snippet print?
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# This code will print one is ["one"], two is ["two"] and three is ["three"]
# one, two and three are local variables that are being reassigned inside the mess_with_vars function

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# This code will print one is ["one"], two is ["two"] and three is ["three"]
# one, two and three are local variables that are being reassigned inside the mess_with_vars function

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

'''
This code will print one is ["two"], two is ["three"] and three is ["one"]
In this case the parameters one, two, and three point to the same list objects in memory as the outer variables one, two, and three
mess_with_vars() performs in-place mutation
'''

'''
Question 4: 
is_dot_separated_ip_address determines whether an input string is an IP address using 4 dot-separated numbers.
is_an_ip_number determines whether a string is a numeric string between 0 and 255 as required for IP numbers.
Fix the code so it returns a false condition and handles the case when the input string has more or less than
4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid.
'''
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True

# Question 5: What do you expect to happen when the greeting variable is referenced in the last line of the code below?
if False:
    greeting = "hello world"

print(greeting)

# This code raises a NameError because the if block never runs.
