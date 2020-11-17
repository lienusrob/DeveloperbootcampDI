#task 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]



# dic1 = dict(zip(keys, values))
# print (dic1)

#task 2
#havent finshised the one from yesterday 




#Exercise 3: Zara
# brand = {
#  	'name': 'Zara',
# 	'creation_date': 1975,
# 	'creator_name': 'Amancio Ortega Gaona',
# 	'type_of_clothes': ['men', 'women', 'children', 'home'],
# 	'international_competitors': ['Gap', 'H&M', 'Benetton'],
# 	'number_stores': 7000,
# 	'major_color': {
# 	'France': 'blue',
# 	'Spain': 'red',
# 	'US': ['pink', 'green']
# }
# }


# brand["number_stores"] =2
# brand['country_creation'] = 'Spain'


# additional_hobbies = ["Sport", "More code"]
#brand['international_competitors'].append("Desigual")

# del brand['creation_date']

#print(brand)
# brand['international_competitors[2]']#stupied error 
# print("Zara has all kinds for clients")
#print(brand['international_competitors'][-1])
#print(brand['international_competitors'])


#print("  keys() :", len(brand.keys())) 
#print("len() method :", len(brand))

#I have to come back part 11 of the question 

#task4 
#i have to translate the list into a dict with values and keys. 
#then loop it 
#use enumerate()
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 
# my_list = []
# my_list = [num for num in users]
# #users1= dict.fromkeys(users, "I")
# print(my_list)

l1 = ["eat","sleep","repeat"] 
s1 = "geek"
  
# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
  
print "Return type:",type(obj1) 
print list(enumerate(l1)) 
  
# changing start index to 2 from 0 
print list(enumerate(s1,2))
