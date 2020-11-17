# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum

# print(listsum([1,3,5,6,10,2000]))

 #tast1

#Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
#Call the function, and make sure the message displays correctly.

def say_hello():

    print("function do this !") 

say_hello()


#task2 
# Exercise 2: What’s Your Favorite Book ?

# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, making sure to include a book title as an argument in the function call.
# def favorite_book(title):
# 		print("my fav book is " + title)

# favorite_book("1984")

# task3 
#Write a function that accepts one parameter (a number X) and returns the value of X+XX+XXX+XXXX.
# def tast3():
# digit = 1
# n = 5
# ones = [ int("1" * i) for i in range(1, n+1)]
# print(ones)

# def sumx(x):
# 	test =[str(x)*i for i in range(1, x+1)]
# 	print "+".join(test)
# 	return sum(map(int, test))

# sumx(1)
# ones = [ int("1" * i) for i in range(1, n+1)]

# print(ones)
#almoste couldnt manage to make it work with x need to convert it to strings but dont know how tto do thatt right now will come back to it later

# Exercise 4 : Some Geography

# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.
#def describe_city(city="Reykjavik", country='Iceland'):
#    output = city + " is in " + country + "."
#    print(output)
#describe_city()
#describe_city("Berlin", "Germany ")
#describe_city("London", "uk")



# Exercise 5 : Let’s Create Some Personalized Shirts !

# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


# def make_shirt(size="large", message="I love python"):
# 	summarizing = (size + message)
# 	print(summarizing)
# make_shirt()
# make_shirt("48 ", "my new message" )
# make_shirt(message="my message.", size="Small ")
# make_shirt("large ", "first statment")
# print(make_shirt)

# Exercise 6 : Magicians …

# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.


# def show_magicians(magicians):
#     """Print the name of each magician in the list."""
#     for magician in magicians:
#         print(magician + " Harry is the greates ")

# magicians = ["Merlin", "Harry", "Peter"]
# show_magicians(magicians)

#Exercise7
# The point of the exercise is to check is a person can retire depending on his age and his gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return it (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age back.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message to the user informing them whether they can retire or not.
# As always, test your code to ensure it works.



# import datetime

# year = None
# while year is None:
#     try:
#         user_input =input('Enter your date of birth (YYYY): ')
#         year = int(user_input)
#     except ValueError:
#         print('try again!')

# print('You have been born {} years ago'.format(datetime.datetime.now().year - year))









# numbers = []

# def loop_function(numbers):
#     x = 6
#     i = 0
#     while i < x:
#         print "At the top i is %d" % i
#         numbers.append(i)

#         i = i + 1
#         print "Numbers now: ", numbers
#         print "At the bottom i is %d\n" % i

#     return numbers

# loop_function(numbers)
# print "The numbers: " 

# for num in numbers:
#     print num












