# Practice Problems: Easy 1
# Question 1: Will the code below raise an error?
numbers = [1, 2, 3]
numbers[6] = 5

'''
This will throw an IndexError because you are attempting to 
assign a value to an out-of-range index. 
'''
# Question 2: How can you determine whether a given string ends with an exclamation mark (!)? 
# Write some code that prints True or False depending on whether the string ends with an exclamation mark.
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(str1.endswith("!")) # True
print(str1[len(str1) - 1] == "!") # True

print(str2.endswith("!")) # False
print(str2[len(str2) - 1] == "!") # False

# Question 3: Show two different ways to create a new string with "Four score and " 
# prepended to the front of the string referenced by famous_words.

famous_words = "seven years ago..."

# String concatenation
new_str = "Four score and " + famous_words
print(new_str) # Four score and seven years ago...

# String interpolation
new_string = f"Four score and {famous_words}"
print(new_string)

# Question 4: Using the following string, print a string that contains the same value, 
# but using all lowercase letters except for the first character, which should be capitalized.
munsters_description = "the Munsters are CREEPY and Spooky."

print(munsters_description.capitalize()) # The munsters are creepy and spooky.

# Question 5: Print the string with the case of all letters swapped:
munsters_description = "The Munsters are creepy and spooky." 
print(munsters_description.swapcase())

# Question 6: Determine whether the name Dino appears in the strings below -- check each string separately:
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

"Dino" in str1 # False
"Dino" in str2 # True

str1.find("Dino") # -1 (not found)
str2.find("Dino") # 41 (starting index)

# Question 7: How can we add the family pet, "Dino", to the following list?
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

flintstones.append("Dino")
flintstones.extend(["Dino"])
flintstones += ["Dino"]

# Question 8: In the previous problem, our first answer added 'Dino' to the list like this:
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])

# Question 9: Print a new version of the sentence given by advice that ends just before the word house. 
# Don't worry about spaces or punctuation: remove everything starting from the beginning of house to the end of the sentence.

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

print(advice.split("house")[0])
print(advice[0: 38])
print(advice.replace(" house training your pet dinosaur.", ""))

# Question 10: Print the following string with the word important replaced by urgent:
advice = "Few things in life are as important as house training your pet dinosaur."

print(advice.replace("important", "urgent"))
