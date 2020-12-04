# Exercise 1 : Favorite Numbers
# Create a set called my_fav_numbers with your favorites numbers.
# Add two new numbers to it.
# Remove the last one.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.


my_fav_numbers = set()

my_fav_numbers.add("1")

my_fav_numbers.add("2")

my_fav_numbers.pop()

print(my_fav_numbers)

friend_fav_numbers=set("2")

my_fav_numbers+my_fav_numbers 

our_fav_numbers = set(my_fav_numbers).union(set(friend_fav_numbers))
print(our_fav_numbers)


# Exercise 2: Tuple
# Given a tuple with integers is it possible to add more integers to the tuple?


# Exercise 3: Print A Range Of Numbers
# Use a for loop to print the numbers from 1 to 20, inclusive. 


for i in range(1, 21):
  print(i)