# ================================================================
# Python Workshop 01 – Python Basics
# ================================================================
# Topics Covered:
# 1. Hello World
# 2. Comments
# 3. Variables
# 4. Data Types
# 5. Input / Output
# 6. Operators
# 7. Strings
#
# Each section includes:
#   - Explanation
#   - Examples
#   - "Try it Yourself" mini-tasks
# ================================================================


# ================================================================
# 1. HELLO WORLD
# ================================================================

# In Python, 'print()' is used to display text or data on the screen.
# Text (called a "string") must be enclosed in either single ('') or double ("") quotes.


print("Hello world!")


# ------------------------------------------------
# TRY IT YOURSELF:
# Write a print statement that says:
# "My first Python program!"
# ------------------------------------------------

print("My first python program")



# ================================================================
# 2. COMMENTS
# ================================================================

# Comments are notes in your code that Python ignores.
# They are used to explain what your code does, making it easier to read.

# this is a comment 

# You can also write multi-line comments using triple quotes (""") or ('''):

"""
This is a multi-line comment.
It can span multiple lines.
Python ignores it when running the program.
"""


# ------------------------------------------------
# TRY IT YOURSELF:
# Write a comment with your name and today’s date.
# ------------------------------------------------



# ================================================================
# 3. VARIABLES
# ================================================================

# A variable is a named storage location in memory used to store data.
# You create a variable when you assign a value to it using '='.
message = "Welcome to Python!"
age = 20
pi = 3.14159
print(message)
print("Age:", age)
print("Pi value:", pi)
# Python is dynamically typed it automatically knows the type and assign it to variables.

print("Type of message:", type(message))
print("Type of age:", type(age))
print("Type of pi:", type(pi))

# Naming rules:
# - Must start with a letter or underscore (_)
# - Can contain letters, numbers, and underscores
# - Case-sensitive (age != Age)
# - Cannot start with a number or use special characters (!, @, etc.)

# Multiple assignment examples:

x, y, z = 1, 2, 3
print("x =", x, "y =", y, "z =", z)

# Assign same value to multiple variables

a = b = c = 100
print(a, b, c)


# Variables can be updated or reassigned

name = "Alice"
print(name)
name = "Bob"  # now it holds a new value
print(name)

# ------------------------------------------------
# TRY IT YOURSELF:
# Create variables: your_name, your_age, and your_city.
# Print them using one print statement.
# ------------------------------------------------



# ================================================================
# 4. DATA TYPES
# ================================================================

# Python has several built-in data types. The most common are:

# 1. Numeric Types

num_int = 10          # Integer
num_float = 10.5      # Float (decimal number)
num_complex = 3 + 4j  # Complex number
print(num_int, num_float, num_complex)

# 2. Boolean Type (True or False)

is_sunny = True
is_raining = False
print("Sunny?", is_sunny)
print("Raining?", is_raining)


# ================================================================
# 3. Sequence Types
# ================================================================

# ------------------------------------------------
# LISTS
# ------------------------------------------------
# Lists are ordered, mutable (changeable) collections.
# You can store multiple items in a single variable.

fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# You can access list items by index (0-based)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])



# Lists are mutable you can modify them after creation:

fruits[1] = "blueberry"
print("After changing second fruit:", fruits)

# Add items

fruits.append("orange")          # adds to the end
fruits.insert(1, "mango")        # inserts at index 1

# Remove items

fruits.remove("apple")           # removes by value
removed = fruits.pop()           # removes last item, returns it
print("Removed item:", removed)
print("After removing items:", fruits)


# List slicing (extract a portion)

print("First two fruits:", fruits[:2])
print("Last two fruits:",fruits[1:])

# Sorting and reversing

numbers = [5, 2, 8, 1, 3]
numbers.sort()        # sorts ascending
print("Sorted list:", numbers)
numbers.reverse()     # reverses order
print("Reversed list:", numbers)

# List length and membership

print("Number of fruits:", len(fruits))
print("Is mango in list?", "mango" in fruits)

# ------------------------------------------------
# TRY IT YOURSELF:
# Create a list of your 4 favorite movies.
# 1. Print the first and last movie.
# 2. Add a new movie.
# 3. Sort the list alphabetically.
# ------------------------------------------------



# ------------------------------------------------
# TUPLES
# ------------------------------------------------
# Tuples are like lists but IMMUTABLE (cannot be changed).

coordinates = (10, 20)
print("Tuple:", coordinates)


# Access by index
print("First coordinate:", coordinates[0])


# Tuples cannot be modified:
# coordinates[0] = 99  #  This will cause an error.
# You can combine tuples
colors = ("red", "green")
new_tuple = coordinates + colors
print("Combined tuple:", new_tuple)

# ------------------------------------------------
# TRY IT YOURSELF:
# Create a tuple with your birth day, month, and year.
# Try to modify one value, observe the error message.
# ------------------------------------------------


# ================================================================
# 4. Mapping Type (Dictionary)
# ================================================================

# Dictionaries store data in key-value pairs.

person = {"name": "Alice", "age": 25, "city": "London"}
print("Dictionary:", person)

# Accessing values by key

print("Name:", person["name"])
print("City:", person.get("city"))  # get() avoids KeyError if key not found

# Adding new key-value pairs

person["email"] = "alice@example.com"
print("After adding email:", person)

# Updating existing keys

person["age"] = 26
print("After updating age:", person)

# Removing items

del person["city"]        # removes by key
print("After deleting city:", person)

# Dictionary methods

print("Keys:", list(person.keys()))
print("Values:", list(person.values()))


# Nested dictionaries (dictionary inside a dictionary)

students = {
    "S001": {"name": "John", "grade": "A"},
    "S002": {"name": "Emma", "grade": "B"}
}
print(students)
print("Nested dictionary example:", students)
print("Emma’s grade:", students["S002"]["grade"])

# ------------------------------------------------
# TRY IT YOURSELF:
# Create a dictionary with keys: brand, model, year.
# Add a new key 'color' and update 'year' to the current one.
# ------------------------------------------------



# ================================================================
# 5. Set Type (unique, unordered)
# ================================================================

# Sets are unordered collections of unique elements (no duplicates allowed)

unique_numbers = {1, 2, 2, 3, 4, 4}
print("Set (no duplicates):", unique_numbers)

# Add and remove elements

unique_numbers.add(5)
unique_numbers.discard(2)
print("After add & discard:", unique_numbers)

# Sets automatically remove duplicates

fruits_set = {"apple", "banana", "apple"}
print("Fruits set:", fruits_set)

# Set operations (like in math)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)          # combines both sets
print("Intersection:", a & b)   # common elements
print("Difference:", a - b)     # elements in a but not in b
print("Symmetric difference:", a ^ b)  # elements in one but not both

# Membership check

print("Is 3 in set a?", 3 in a)

# Convert list to set to remove duplicates

numbers_list = [1, 2, 2, 3, 3, 4]
unique = set(numbers_list)
print("Unique from list:", unique)

# Casting: converting between types

x = 5
print(float(x))  # int to float
print(str(x))    # int to string
print(int(3.7))  # float to int (truncates)


# ------------------------------------------------
# TRY IT YOURSELF:
# Create two sets of your favorite foods and your friend’s favorite foods.
# Find the foods you both like (intersection) and the foods only you like (difference).
# ------------------------------------------------



# ================================================================
# 5. INPUT / OUTPUT
# ================================================================

# INPUT

name = input("Enter your name: ")
print("Hello,", name)

# You can convert it using int(), float(), etc.
# Example:

age = int(input("Enter your age: "))
print("You are", age, "years old.")

# OUTPUT

# The print() function can display variables or formatted strings.
# Comma-separated printing automatically adds spaces:

print("Python", "is", "fun!")

# You can use + for string concatenation (convert numbers to strings first)

print("I am " + str(20) + " years old.")

# Formatted printing using f-strings (recommended):

name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")

# use format() function to print 

print("My name is {} and I am {} years old".format(name,age))

# You can also print variables 

name = "Alice"
print("Hello,", name)

# You can control what appears at the end of the print using the 'end' parameter:

print("This is on one line", end=" ")
print("because we used end=' '")

# 'sep' changes the separator between items
print("A", "B", "C", sep=" - ")

# ------------------------------------------------
# TRY IT YOURSELF:
# Ask the user for their name and favorite food.
# Then print: "Hello <name>, your favorite food is <food>!"
# ------------------------------------------------



# ================================================================
# 6. OPERATORS
# ================================================================

# Operators are symbols that perform operations on values and variables.

# 1. Arithmetic Operators

a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)  # gives integer result
print("Modulus:", a % b)          # remainder
print("Exponentiation:", a ** b)  # power

# 2. Assignment Operators

x = 5
x += 3  # same as x = x + 3
print("After += :", x)

# 3. Comparison Operators

print("Is 5 equal to 3?", 5 == 3)
print("Is 5 greater than 3?", 5 > 3)
print(5>=3,5>=5,3<=5)
print("Is 5 not equal to 3?", 5 != 3)

# 4. Logical Operators

a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

# 5. Membership Operators

print("2 in [1,2,3] ?", 2 in [1, 2, 3])
print("5 not in [1,2,3] ?", 5 not in [1, 2, 3])



# ------------------------------------------------
# TRY IT YOURSELF:
# Create two numbers and print their sum, difference, and product.
# Try checking if a number exists in a list using 'in'.
# ------------------------------------------------



# ================================================================
# 7. STRINGS
# ================================================================

# A string is a sequence of characters enclosed in quotes.

text1 = "Hello"
text2 = 'World'
print(text1, text2)

# Multi-line strings use triple quotes:

multiline = """This is
a multi-line
string."""
print(multiline)

# Including quotes inside strings:

quote1 = "She said, 'Hello!'"
quote2 = 'He replied, "Hi there!"'
print(quote1)
print(quote2)

# Strings act like arrays (you can access characters by index)

word = "Python"
print("First letter:", word[0])
print("Last letter:", word[-1])

# Slicing: extract parts of strings

print("words from index 0 to 2  =", word[0:3])  
print("words from start to index 3 =", word[:4])    
print("word from index 2 to end =", word[2:]) 
   
# Common string methods

s = "  Hello, World!  "
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Strip spaces:", s.strip())
print("Replace:", s.replace("World", "Python"))
print("Split:", s.split(","))

# Concatenation (+) and repetition (*)

a = "Python"
b = "Rocks"
print(a + " " + b)
print(a * 3)  # repeats string

# Length of string

print("Length of text1:", len(text1))

# Escape characters
print("New line:\nSecond line")
print("Tab:\tIndented text")
print("Backslash:\\ Inserts a literal backslash")


# ------------------------------------------------
# TRY IT YOURSELF:
# Create a string with your full name.
# Print:
# - only the first name
# - the length of your full name
# - the name in all uppercase letters
# ------------------------------------------------





# ================================================================
# END OF WORKSHOP
# ================================================================
# print("\n End of Python Workshop 01 – Great job learning the basics!")
