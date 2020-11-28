
# Exercise 1 : Built-In Functions

# Python has many built-in functions, and if you do not know how to use it, you can read document online. 
# But Python has a built-in document function for every built-in functions.

# Write a program to print some Python built-in functions documents, such as abs(), int(), raw_input().
# And add documentation for your own function

 
# xy = abs(-7.25) 
# print(xy)
#would display 7.25 as an abselute value. in other words returns the abusliute value of a speific number. 

#input function
#allowes user to enter details and these details can be stored and be used again. 

# print('type ')
# x = input()
# print('this its what is happinging, ' + x)



# List of strings 

# def plusseven(num):
# 	return num + 7

# numbers = [1,2,3]
# print(list(map(plusseven, numbers)))

# map() can listify the list of strings individually 


# tast 2.

# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)
# >>> str(c1)
# '5 dollars'
# >>> int(c1)
# 5
# >>> repr(c1)
# '5 dollars'
# >>> c1 + 5
# 10
# >>> c1 + c2
# 15
# >>> c1 
# 5 dollars
# >>> c1 += 5
# >>> c1
# 10 dollars
# >>> c1 += c2
# >>> c1
# 20 dollars
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>



#we need to make a class. 
# define a function 
# add self/soule inside, and add a currency and a value inside. Since the quesiton is displaying this: 
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)
#the Capital C is telling we need to creat a class. And the Shekels and dollars are indicating that we need 2 attributes
#(i dont know if that is the right term) but we need a value in our class.  

class Currency: 

	def __init__(self, currrency, value):
		self.currrency= currrency
		self.value= value 
	#def __repr__(self): # it think here i could have also used 
		#return "currrency: {}, value {}".format(self.currrency, self.value)
	
	def __str__(self): # it think here i could have also used  str((self)) or something like this. since the str function calls 
	#the __str__ dunder function so tecnically they do the same 
		return "currrency1: {}, value {}".format(self.currrency, self.value)
# i am defining the new varibals which are assinged to the class Currency therefore they must have a "currency" & and a value 
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)
print (c1)
print (c2)
print (c3)
print (c4)
# we want to display the class oof c1 i am sure there is a better way how to do that. bu ti dont know it.
c1str= str(c1)
print(type(c1str))
#and afterwards i am lost


# def __add__(self, other):
# 		return Currency(self.vaule + 5)


#task3
import datetime

# present = datetime.datetime.now()
# future = datetime.datetime(2020, 12, 31,)
# difference = future - present
# print(difference)

# # #task4
# # Exercise 4:

present= datetime.datetime.now()
holiday = datetime.datetime(2020,12,24)
holidays = holiday - present
print (holidays) 

# c1int = int(c1)
# print(c1int)
#print(type(c4)) NOT WORKING 
# from faker import Faker
# fake = Faker('it_IT')
# for _ in range(10):
#     print(fake.name())





