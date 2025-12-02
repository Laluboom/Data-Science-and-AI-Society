# ---------------------------------------------------------------------------------------------
# Calculator Task 
# ----------------------------------------------------------------------------------------------

# ========================================================================= 
#                     CHALLENGE: SIMPLE CALCULATOR BUILDER 
#  ========================================================================= 

# SCENARIO: 
# Build a basic calculator that takes two numbers from the user and performs 
# various operations on them. Display the results in a formatted way. 

 

# YOUR TASKS: 
#     1. Ask the user for their name and greet them 
#     2. Get two numbers from the user (use float for decimals) 
#     3. Perform ALL arithmetic operations on these numbers: 
#        - Addition 
#        - Subtraction 
#        - Multiplication 
#        - Division 
#        - Floor Division 
#        - Modulus (remainder) 
#        - Exponentiation (first number to the power of second) 
#     4. Compare the two numbers: 
#        - Check if first is greater than second 
#        - Check if they are equal 
#        - Check if they are not equal 
#     5. Display all results in a neat, formatted way 

 

# EXPECTED OUTPUT EXAMPLE: 

#     Enter your name: Alice 
#     Hello, Alice! Welcome to the Calculator! 
#     Enter first number: 10 
#     Enter second number: 3 

#     ===== CALCULATION RESULTS ===== 
#     10.0 + 3.0 = 13.0 
#     10.0 - 3.0 = 7.0 
#     10.0 × 3.0 = 30.0 
#     10.0 ÷ 3.0 = 3.333... 
#     10.0 // 3.0 = 3.0 
#     10.0 % 3.0 = 1.0 
#     10.0 ** 3.0 = 1000.0 

#     ===== COMPARISONS ===== 
#     Is 10.0 > 3.0? True 
#     Is 10.0 == 3.0? False 
#     Is 10.0 != 3.0? True 


# ============================================================================ 
# YOUR CODE HERE 
# ============================================================================ 
# Task 1: Get user's name and greet them 

 
# Task 2: Get two numbers from the user 

 
# Task 3: Perform arithmetic operations 


# Task 4: Perform comparisons 

 
# Task 5: Display results in formatted way 


# ============================================================================ 
# Hints: 
# CONCEPTS YOU'LL USE: 

#     - input() for getting user data 
#     - int() and float() for type conversion 
#     - Arithmetic operators: +, -, *, /, //, %, ** 
#     - Comparison operators: >, <, ==, != 
#     - f-strings for formatted output 
#     - print() with sep and end parameters 
# ============================================================================ 
 

 
# ----------------------------------------------------------------------------------------------
# Flight data Game 
# ----------------------------------------------------------------------------------------------

# Given flight data 
flights = { "FL001": {"origin": "NYC", "destination": "LAX", "time": (8, 13), "price": 250}, 
"FL002": {"origin": "LAX", "destination": "CHI", "time": (14, 18), "price": 180}, 
"FL003": {"origin": "NYC", "destination": "MIA", "time": (9, 12), "price": 200}, 
"FL004": {"origin": "MIA", "destination": "LAX", "time": (13, 17), "price": 220}, 
"FL005": {"origin": "CHI", "destination": "NYC", "time": (19, 22), "price": 190}, 
"FL006": {"origin": "LAX", "destination": "NYC", "time": (15, 20), "price": 260} } 
print("=" * 70) 
print("FLIGHT ROUTE OPTIMIZER") 
print("=" * 70) 
print() 
# ============================================================================ 
# TASK 1: Create a SET of all unique airports 
# ============================================================================ 
print("TASK 1: All Airports") 
print("-" * 70) 

# YOUR CODE HERE 
# Hint: Loop through flights dictionary, add both origin and destination to a set 
# all_airports = set() 

# print("All airports:", all_airports) 

print() 

 
# ============================================================================ 
# TASK 2: Find all flights FROM "NYC" 
# ============================================================================ 
print("TASK 2: Flights from NYC") 
print("-" * 70) 

# YOUR CODE HERE 
# Hint: Loop through flights, check if origin is "NYC", add flight code to list 
# flights_from_nyc = [] 

 

 
# print("Flights from NYC:", flights_from_nyc) 
print() 

# ============================================================================ 
# TASK 3: Find all flights TO "LAX" 
# ============================================================================ 
print("TASK 3: Flights to LAX") 
print("-" * 70) 

# YOUR CODE HERE 
# Hint: Loop through flights, check if destination is "LAX" 
# flights_to_lax = [] 
# print("Flights to LAX:", flights_to_lax) 
print() 

# ============================================================================ 
# TASK 4: Check for time conflicts (same origin, same departure hour) 
# ============================================================================ 
print("TASK 4: Time Conflict Detection") 
print("-" * 70) 
 

# YOUR CODE HERE 
# Hint: Compare departure times (time[0]) for flights with same origin 
# has_conflict = False 

 

# print("Time conflict found:", has_conflict) 
print() 

# ============================================================================ 
# TASK 5: Find valid connecting flights through LAX 
# ============================================================================ 
print("TASK 5: Valid Connections") 
print("-" * 70) 

# YOUR CODE HERE 
# Hint: Find flights TO LAX, then flights FROM LAX 
# Check if arrival time + 1 hour <= departure time 

# valid_connections = [] 

 

 
# print("Valid connections:", valid_connections) 
print() 

 
# ============================================================================ 
# TASK 6: Calculate round trip price NYC -> LAX -> NYC 
# ============================================================================ 
print("TASK 6: Round Trip Price") 
print("-" * 70) 

# YOUR CODE HERE 
# Hint: Find NYC to LAX price (FL001) + LAX to NYC price (FL006) 
# round_trip_price = 0 

 
# print(f"NYC -> LAX -> NYC total price: ${round_trip_price}") 
print() 

# ============================================================================ 
# TASK 7: Find all cities reachable from NYC (direct + one-stop) 
# ============================================================================ 
print("TASK 7: Reachable Destinations") 
print("-" * 70) 

# YOUR CODE HERE 


# ============================================================================ 
# Hint: Find direct destinations from NYC, then destinations from those cities 
# reachable_cities = set() 

# print("Reachable from NYC:", reachable_cities) 
print() 
print("=" * 70) 
# ============================================================================ 

# ---------------------------------------------------------------------------------------------
# ODD & EVEN NUMBER ORGANIZER
# ----------------------------------------------------------------------------------------------
# SCENARIO:
# You are creating a function that organizes numbers into two groups:
# odd numbers and even numbers.
#
# The program should:
#   - Take a list of numbers
#   - Loop through the list
#   - Use if/else to test whether each number is odd or even
#   - Add each number to the correct list (or set)
#   - Return both results
#

# EXPECTED OUTPUT EXAMPLE:
#   Input: [1, 2, 3, 4, 5, 6, 7]
#   Even numbers: [2, 4, 6]
#   Odd numbers: [1, 3, 5, 7]
# ============================================================================

# YOUR CODE HERE:
# 1. Define a function called separate_numbers(numbers)



# 2. Create two empty lists (or sets) — one for evens, one for odds



# 3. Loop through the given list



# 4. Use if/else to check each number



# 5. Add it to the right list



# 6. Return both lists



# 7. Call the function and print the result