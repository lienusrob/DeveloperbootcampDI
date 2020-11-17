#challange1
#list_name.insert(index, element)logic behind it 
#practical 
# list_1 = [ 1, 2, 3, 4, 5, 6, 7 ]   
# list_1.insert(1, 10)  
# print(list_1)  
#challange2 
# a_string = " hello world "
# b_string=a_string.count(" ")
# print(b_string)
#challange3 need to go over this 

# def count_by_case(string):
#     upper = sum(letter.isupper() for letter in string)
#     lower = sum(letter.islower() for letter in string)
#     return lower, upper

# string = " helloo what is going on"
# lower, upper = count_by_case(string)
# print("{!r} contains {} upper and {} lower case letters".format(string, upper, lower))
#challange4 without build in function 
#Write a function to find the max of a list
# my_list = ([0,1,3,50])
# def find_max(my_list):
# 	big = my_list[0]
# 	for num in my_list:
# 		if num > big:
# 			big = num 
# 	return big
# Y=find_max(my_list)
# print(Y)
# challange5
# num = 100 
# def factiorial(num):
# 	if num == 0:
# 		return 1 
# 	else:
# 		return num*factiorial(num-1)

# X =factiorial(num)
# print (X)

# with build in function 
# import math
# print (math.factorial(4))
# num=4
# he_lp = 1
# for i in range(1, num+1):
#     he_lp = he_lp*i
# print(he_lp)


#challange6 
# MySum=([1,5,4,2])

# def listsum(MySum):
#     theSum = 0
#     for i in MySum:
#         theSum = theSum + i
#     return theSum
# the_sum=listsum(MySum)
# print(the_sum)

#challange7 modified 
#And I want you to count how many letter "a" are in the list.

# mylist = ["a", "b", "a", "c", "a", "d"]
# def findx(mylist):
# 	num = mylist[0]
# 	for a in mylist:
# 		if num == a:
# 			num=a
# 	return num+a
# Y=findx(mylist)
# print(Y)

# mylist = ["a", "b", "a", "c", "a", "d"]
# count = 0
  
# for i in mylist: 
#     if i == 'a': 
#         count = count + 1
# print (str(count)) 


#challange8 need to look at it later

#Exercise 9
#Write a function to find if an array is monotonic (sorted either ascending of descending)
# Python3 program to find sum in Nth group 

# Check if given array is Monotonic 

#define a array
#define a function. 
	#for in loop, though the range of the list. and check if the following number is increasing
	#either use a else if function or or the OR 
	#return 
	#print 

#not working the ocde 
# num = ["1", "2", "3"]
# def monotonic(element):
# 	return (num(all(num[i])<=num[i+1] for i in range(len(num)-1)) or 
# 		all(num[i]>=num[i+1] for i in range(len(num)-1)))

# print(monotonic(num))

#task11

#Write a function that prints the longest word in a list.
# def findMaximum(word):
#     li=word.split()
#     li=list(li)
#     op=[]
#     for i in li:
#         op.append(len(i))
#     l=op.index(max(op))
#     print (li[l])
# findMaximum(input("Enter your word:"))


#task13
sentence = 'Do or do not there is no try'
# k=2
# sum_over_k(sentence,k)
# # 3
print(type(sentence))


# def findMaximum(word):
#     x = 0 
#     #sentence=word.split()
   
#     for i in sentence:
#         x = x < 2 + i 
#     return x
# x=findMaximum(sentence)
# print(x)
# def findMaximum(sentence):
#     over = sum(sentencce )








