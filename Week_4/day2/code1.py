# Exercise 1 : Favorite Numbers
# Create a set called my_fav_numbers with your favorites numbers.
# Add two new numbers to it.
# Remove the last one.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.


# my_fav_numbers = set()

# my_fav_numbers.add("1")

# my_fav_numbers.add("2")

# my_fav_numbers.pop()

# print(my_fav_numbers)

# Exercise 2: Tuple
# Given a tuple with integers is it possible to add more integers to the tuple?


# Exercise 3: Print A Range Of Numbers
# Use a for loop to print the numbers from 1 to 20, inclusive. 


# for i in range(1, 21):
#   print(i)
# Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way of generating a sequence of floats?
# Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.

# x=[x * 0.5 for x in range(0, 10)]

# print(x)


# Exercise 5: Shopping List
# Consider this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Put “Kiwi” at the end of the list.
# Add “Apples” at the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.pop(-1)

# basket.append("Kiwi")
# basket.insert(0,"Apples")
# sumbasket=basket.count("Apples")
# basket.clear()
# print(basket)
# print(sumbasket)


# Exercise 6 : Loop
# Write a while loop that will keep asking the user for 
# input until the input is the same as your name.

# name = " " 
# while name != "Rob":
#     name=input("guess my name")

# print("Finished")

# Given a list, use a while loop to print out every 
# element which has an even index.
# number=0
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# while(number <len(basket)):
#   if number %2 == 0:
#    print(basket[number], end = " ")
#   number+=1


#Make a list of the multiples of 3 from 3 to 30.
# Use a for loop to print the numbers in your list.
# #task8Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

# for i in range(3, 31,3):
#    print(i)

#task9
#Use a for loop to find numbers between 
# 1500 and 2700, which are divisible by 7 and multiples of 5.
# newlist=[]
# for i in range(1500, 2700):
#   if (i%5==0) and (i%7==0): 
#     newlist.append(str(i))
#     print(newlist)



# Ask the user to type in his/her favorite fruit(s) (one or several fruits).
# Hint : Use the input built in method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list. (How can we ‘convert’ a string of words into a list of words?).
# # Now that we have a list of fruits, ask the user to type in the name of any fruit.
# # If the user’s input is a fruit name existing in the list above, print “You chose one of your favorite fruits! Enjoy!”.
# # If the user’s input is NOT a fruit name existing in the list above, print, “You chose a new fruit. I hope you enjoy it too!”.
# # Bonus: Display the list in a user friendly way : add the word “and” before the last fruit in the list – but only if there are more than 1 favorites!
# Fav = input('type your favorite fruits and separate with space?')
# yourfav=[]
# favfruit=input(" what is your fav fruit")
# print("you have choosen your fav")
# yourfav.append(favfruit)
# print("your fav are ")
# 
# for favfruit in yourfav: 
#   if favfruit==yourfav:
#     print("another try" )
#   else
#   for favfruit in yourfav: 
#   if favfruit==yourfav:
#     print("you have guest my fav fruit")

# Exercise 11: Who Ordered A Pizza ?
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exit print all the toppings on the pizza and what the total is (10 + 2.5 for each topping)
# pizza=[]
# pizzaone=[]
# while pizza != "quit":
#     pizza=input("topping?")
#     pizzaone.append(pizza)
#     print( pizza )

# print(len(pizzaone)*2.5+10)


# Exercise 12: Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Apply it to a family, ask the user what the age of each of the people that want a ticket is.
# Store the total cost of all the tickets for this group and print it out.
# A group of teenagers is coming to your 
# movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which one can see the movie.
# Tip: Try to add the allowed ones to a list.

# ag=input(" What age you")
# age=int(ag)
# if age < 3: 
#     print("its for free")
# elif age <12 and age>3:
#     print(10)
# elif age <12: 
#     print(15)


# Exercise 13 : Who Is Under 16?
# This time you have a list of users, and you want to remove every user that is below 16 years old.
# oage=[]
# age=[5,22, 20]
# for i in age: 
#   if i >16:
#     oage.append(i) 
# print(oage)
# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.



# At the end, print the final list.
# Exercise 14: Family Members
# Using a while loop keep asking a user for input, these inputs will be used to control a menu
# On the menu we will have 4 options:
# Add a name
# If the user selects this ask for the name to add
# Remove an existing name
# If the user selects this ask for the name to remove
# View family members
# Print a nice list of the family members names
# Exit

