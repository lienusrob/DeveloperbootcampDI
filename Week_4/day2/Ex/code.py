# Create a set called my_fav_numbers with your favorites numbers.
# Add two new numbers to it.
# Remove the last one.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.
#task1
# my_fav_numbers = set([9, 3]) 
# my_fav_numbers.add("8")
# my_fav_numbers.add("4")
# my_fav_numbers.discard(3)
# friend_fav_numbers =set ([3, 1])
# our_fav_numbers = set(my_fav_numbers).union(set(friend_fav_numbers))
# print(our_fav_numbers)
#task2
#Given a tuple with integers is it possible to add more integers to the tuple?
#no becuase its immutable we could but we would creat a copy of it and it would not be saved anywhere 
#task3 

# fruits = ['apple', 'banana', 'kiwi', 'pear']

# for fruit in fruits:
#   print(fruit)
# x = range(21)
# for n in x:
#   print(n)

#another way easier 
# for i in range(1, 21,):
#    print(i)


#task4
# import decimal

# def float_range(start, stop, step):
#   while start < stop:
#     yield float(start)
#     start += decimal.Decimal(step)

# print(list(float_range(0, 20.5, '0.5')))
#need to ask for help 

#task5
# Consider this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Put “Kiwi” at the end of the list.
# Add “Apples” at the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("Banana")
# # print(basket)
# addbasket = ["Kiwi"]
# sumbaseket= basket + addbasket
# # print(sumbaseket)
# # print(len(sumbaseket))
# # print(sumbaseket.count("Apples"))
# # sumbaseket.clear 
# # print(sumbaseket)
# print(sumbaseket)	
# sumbaseket.clear()
# print(sumbaseket)	
# task7
# Write a while loop that will keep asking the user for input until the input is the same as your name.
# Name  = ''
# while Name != 'Rob':
#   Name = input('Guess my name ? ')

# print('You guessed the right name!')


#task7

# Given a list, use a while loop to print out every element which has an even index.

# num=0
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# while(num < len(basket)): 
#     # checking condition 
#     if num % 2 == 0: 
#        print(basket[num], end = " ") 
#     # increment num   
#     num += 1


# #task8Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
# l = [i for i in range(3, 31) if i % 3 == 0]
# print(l)
# for i in range(3, 31,3):
#    print(i)

#task9
#Use a for loop to find numbers between 1500 and 2700, which are divisible by 7 and multiples of 5.
# result=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         result.append(str(x))
# print (','.join(result))


#another way 
# new_list = []
# for i in range(1500, 2701):
#     if (i%7==0) and (i%5==0):
#         new_list.append((i))
# print(new_list)
#task10 

# Ask the user to type in his/her favorite fruit(s) (one or several fruits).
# Hint : Use the input built in method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list. (How can we ‘convert’ a string of words into a list of words?).
# # Now that we have a list of fruits, ask the user to type in the name of any fruit.
# # If the user’s input is a fruit name existing in the list above, print “You chose one of your favorite fruits! Enjoy!”.
# # If the user’s input is NOT a fruit name existing in the list above, print, “You chose a new fruit. I hope you enjoy it too!”.
# # Bonus: Display the list in a user friendly way : add the word “and” before the last fruit in the list – but only if there are more than 1 favorites!
# Fav = input('type your favorite fruits and separate with space?')

# def Convert(string): 
#     Fav = list(string.split(" ")) 
#     return Fav
# favlist=(Fav.split(" "))
# print (type(favlist))


# # # Given string
# # print("Given string", Fav)
# # print(type(Fav))
# # # String to list
# # res = Fav.strip('][').split(', ')
# # # Result and its type
# # print("final list", res)
# # print(type(res))
# input1=""
# while input1 != favlist:
# 	favlist = input("type in any fruit")
# print("you guessed my fav fruit")

#code is broken grrrrr 



