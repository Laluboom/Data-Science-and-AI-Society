# ----------------------------------------------------------------------------------------------
# Output a Shape : 
# ----------------------------------------------------------------------------------------------

"""

Create this shape in your output terminal:  

      * 

     *** 

    ***** 

   ******* 

    ***** 

     *** 

      * 

"""

# Hint: 
# print("h")
# print("hh")

# YOUR CODE : 


# ----------------------------------------------------------------------------------------------    
# List manipulation :  
# ----------------------------------------------------------------------------------------------
# SCENARIO: 
# You're building a shopping list manager. You start with a basic list of items, 
# but you need to modify it based on what you remember and what you need. 
# GIVEN: 
#     items = ['bread', 'milk', 'eggs'] 

# YOUR TASKS: 

#     1. Add 'butter' to the end of the list 
#     2. Insert 'cheese' at position 1 (second position) 
#     3. Remove 'milk' from the list 
#     4. Remove the last item and store it in a variable called 'last_item' 
#     5. Print the final list 

 
# EXPECTED OUTPUT: 

#     Starting list: ['bread', 'milk', 'eggs'] 
#     Removed last item: [whatever the last item is after your modifications] 
#     Final list: [your final list after all modifications]  


# ============================================================================ 
# YOUR CODE HERE 
# ============================================================================ 

#  1. Add 'butter' to the end of the list 




#  2. Insert 'cheese' at position 1 (second position) 



#  3. Remove 'milk' from the list 




#  4. Remove the last item and store it in a variable called 'last_item' 




#  5. Print the final list 




# Hints (from the lesson): 

#     - .append()    : Add item to end 
#     - .insert()    : Insert item at specific index 
#     - .remove()    : Remove item by value 
#     - .pop()       : Remove and return last item (or item at index)


# ----------------------------------------------------------------------------------------------
# Reveal the word : 
# ----------------------------------------------------------------------------------------------

def reveal_secret(): 
    # s = "" 
    # s += chr(98) + chr(97) 
    # s = s.replace("sa", "ka") 
    # s += chr(98) + chr(97) 
    # s += chr(98) + "o" 
    # s = s[::-1] 
    # s += chr(111) + chr(101) + chr(121) 
    # s = s.replace("b", "d") 
    # return s 
    return "Uncomment to decode" 

print(reveal_secret()) 

# ============================================================================ 
# Hint - Some Lines are Misleading
# ============================================================================ 

# ----------------------------------------------------------------------------------------------
# Fix the order of the story :
# ----------------------------------------------------------------------------------------------
"""
part@1 = "The book glowed with a strange light and whispered secrets of variables and functions."
part 2 = "Days turned into weeks, and weeks into months."
3rd_part = "Once upon a time, in a land far away, there lived a young programmer named Zoya."
part4 = "And from that day forward, Zoya continued to code, inspiring others to follow their dreams."
Part5 = "One day, while exploring an ancient library, Zoya discovered a mysterious book about Python."
_part6 = "Excited by this discovery, Zoya began to learn the magical language."
PART7 = "Finally, after much hard work and dedication, Zoya created a program that could solve any problem."
part8! = "Zoya practiced every single day, solving puzzles and building small programs."
part-9 = "Zoya had always dreamed of creating something amazing with code."
part10 = "The entire kingdom celebrated Zoya's achievement and declared it a triumph of human creativity."

print(part@1, part 2, 3rd_part, part4, part5, _part6, PART7, part8!, part-9, part10)
"""

# Hint : do all the names look right to you?
# Naming rules:
# - Must start with a letter or underscore (_)
# - Can contain letters, numbers, and underscores
# - Case-sensitive (age != Age)
# - Cannot start with a number
# - Cannot use special characters (!, @, etc.)