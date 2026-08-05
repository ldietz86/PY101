# Question 1: Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]

numbers.clear()
print(numbers) # []

while numbers:
    numbers.pop()

# Question 2: What will the following code output?
print([1, 2, 3] + [4, 5]) # [1, 2, 3, 4, 5]

# The + operator to concatenate two lists. This operation merges the second list into the first one, producing a new combined list.

# Question 3: What will the following code output?
str1 = "hello there"
str2 = str1 # str2 references the same string object as str1: "hello there"
str2 = "goodbye!" # str2 is reassigned and now references the string object "goodbye"
print(str1) # hello there

# Question 4: What will the following code output?
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1) # [{'first': 42}, {'second': 'value2'}, 3, 4, 5]

'''
The copy() method creates a shallow copy of my_list1 meaning my_list2 now contains a duplicate of
the top-level objects in my_list1, but nested objects are shared.
my_list2[0]['first'] = 42 mutates the shared dictionary at index 0, so the change is visible in the original and copy.
'''

# Question 5: The following function unnecessarily uses two return statements to return boolean values. 
# Can you rewrite this function so it only has one return statement and does not explicitly use either True or False?
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid(color):
    return color in ["blue", "green"]
