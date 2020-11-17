
#task1 
# still not working need to make the string to a list i think
# class Cat:
#     def __init__(self, name, age,):
#         self.name = name
#         self.age = age
# def oldest_cat(cat_list):
#     cat_list[0] = Cat("",-1)
#     for cat in cat_list:
#         if cat.age > max_cat.age:
#             max_cat = cat
#             return cat

# cat1 = Cat("Lis", 3,)
# cat2 = Cat("Isi", 4, )
# cat3 = Cat("mup", 6, )


# cat_list0=[cat1, cat2, cat3]
# cat_list=list(cat_list0)
# print(oldest_cat(f"The oldest cat is {cat_list} years old."))

#task2 
# Exercise 2 : Dogs

# Create a class Dog.
# In this class, create a method __init__, that takes two parameters : nameand height. This function instantiates two attributes, which values are the parameters.
# Create a method named bark that prints “ goes woof!”
# Create a method jump that prints the following “ jumps cm high!” where x is the height*2.
# Outside of the class, create an object davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog by calling the methods.
# Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog by calling the methods.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


# class Dog:

    def __init__(self, name, height):  
        self.name = name
        self.height = height

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.height) + " cm tall")

    def jump(self):
    		print(self.height*2 + "jumps cm high")

davids_dog = Dog("Rex", 50)


bob = Dog("bob", "2")

print(bob.name, bob.height)
print(davids_dog.name, davids_dog.height)

Exercise 3 : Who’s The Song Producer ?

# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics(a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the method sing_me_a_song. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven class Song(object):


# class Song:
# 	def __init__(self, lyrics):
# 		self.lyrics = lyrics
# 	def sing_me_a_song(self):
# 		for line in self.lyrics:
# 			print (line)
# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# print (stairway.sing_me_a_song())

# Exercise4 

animals = ["Ape", "Cat", "Bear", "Cougar", "Baboon", "Eel", "Emu", "Bat"]
animals = sorted(animals)
sorted_animals = {}
key = 1
starting_letter = animals[0][0]   #A
for animal in animals:
	#check starting letter
	if animal[0] != starting_letter:
		key += 1
		starting_letter = animal[0]
	if key not in sorted_animals:
		sorted_animals[key] = animal
	else:  
		if not isinstance(sorted_animals[key], list):
			sorted_animals[key] = [sorted_animals[key]]
		sorted_animals[key].append(animal)
print(sorted_animals)
# {
# 	1: 'Ape', 
# 	2: ['Baboon', 'Bat', 'Bear'], 
# 	3: ['Cat', 'Cougar'], 
# 	4: ['Eel', 'Emu']
# }








