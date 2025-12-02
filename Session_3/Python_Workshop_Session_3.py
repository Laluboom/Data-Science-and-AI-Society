# ================================================================
# Python Workshop 03 – Functions and Classes
# ================================================================
# Topics Covered:
# 1. Functions
# 2. Introduction to Classes and Objects
# 3. Defining and Using Classes
# 4. Constructors and Methods
#
# Each section includes:
#   - Explanation
#   - Examples
# ================================================================


# ================================================================
# 4. FUNCTIONS
# ================================================================
# Functions are reusable blocks of code.
# They help organize your program into smaller, manageable parts.
#
# Syntax:
# def function_name(parameters):
#     code to run
#     return something (optional)
# ---------------------------------------------------------------

# Example 1: Simple function

def greet(name):
    print("Hello,", name + "!")

greet("Alex")
greet("Visesh")


# Example 2: Function with return value

def square(num):
    return num * num
a = square(3)
print(a+3)



# Example 3: Multiple parameters

def calculate_total(price, tax_rate=0.2):
    total = price + (price * tax_rate)
    return total

print("Total price:", calculate_total(100,0.3))


# Example 4: Combining loops + if + functions

def check_even_numbers(numbers):
    for n in numbers:
        if n % 2 == 0:
            print(n, "is even")
        else:
            print(n, "is odd")
numbers = [1, 2, 3, 4, 5]
check_even_numbers(numbers)

numbers = [1, 2, 3, 4, 5]

def even(number_1):
    if number_1 % 2 == 0:
        print(number_1, "is even")
    else:
        print(number_1,"is odd")

for number in numbers:
    even(number)

def random(number,odds,number3=50):
    if number > odds:
        print("yay")
    else:
        print(number3)
    return "hi"

print(random(5,8,30,7))

# ================================================================
# 2. INTRODUCTION TO CLASSES AND OBJECTS
# ================================================================
# Classes let you bundle data (attributes) and behavior (methods) together.
# An object is an instance of a class.
#
# Syntax:
# class ClassName:
#     def __init__(self, parameters):
#         # constructor code
#     def method_name(self, parameters):
#         # method code
# ---------------------------------------------------------------

# Example 1: Simple class definition
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says: Woof!")

# Creating objects (instances)
dog1 = Dog("Buddy")
dog2 = Dog("Luna")
dog3 = ("Alex")

dog1.bark()
dog2.bark()


# ================================================================
# 3. DEFINING AND USING CLASSES
# ================================================================
# You can add multiple attributes and methods to describe real-world objects.
# Each instance stores its own data.
# ---------------------------------------------------------------

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # default attribute
        print("this works")

    def drive(self, km):
        self.mileage += km
        print(f"The {self.brand} {self.model} drove {km} km.")

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} - {self.mileage} km")

# Create car objects
car1 = Car("Tesla", "Model 3", 2023)
car2 = Car("Toyota", "Corolla", 2020)

car1.drive(50)
car2.drive(120)
car1.display_info()
car2.display_info()


# ================================================================
# 4. CONSTRUCTORS AND METHODS
# ================================================================
# The __init__() method is the constructor. It runs automatically
# when an object is created.
#
# Methods are just functions defined inside a class.
# ---------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited £{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew £{amount}")
        else:
            print("Insufficient funds!")

    def show_balance(self):
        print(f"Balance for {self.owner}: £{self.balance}")

# Example usage
account1 = BankAccount("alex", 100)
account1.deposit(50)
account1.withdraw(30)
account1.show_balance()


# ================================================================
# 5. INHERITANCE
# ================================================================
# Inheritance allows one class (child) to use the attributes and methods
# of another class (parent).
# ---------------------------------------------------------------

# Example: Animal is the parent class, Dog and Cat inherit from it
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound.")

class Dog(Animal):
    def speak(self):
        print(self.name, "barks!")

class Cat(Animal):
    def speak(self):
        print(self.name, "meows!")

# Create objects
fox = Animal("Max")
cat = Cat("Mimi")
dog = Dog("Rocky")

dog.speak()
cat.speak()
fox.speak()



# ================================================================
# END OF WORKSHOP
# ================================================================
# Key Takeaways:
# - Functions make your code reusable and organized.
# - Classes combine data and behavior.
# - The constructor (__init__) initializes new objects.
# - Inheritance helps avoid repetition and promotes reusability.
# ================================================================
