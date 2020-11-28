
# #Task 1
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# class Siberian(Cat):
#     def sing(self, sounds):
#         return f"{sounds}"

# my_cats = [Bengal("isi", 2), Chartreux("lisi", 1 ), Siberian("hello", 3)]

# my_pets = Pets(my_cats)

# my_pets1=my_pets.walk()

# print (my_pets1)

# Create a class named Dog with the attributes name, age, weight
# Implement the following methods for the class:
# bark: returns a string of “ barks”.
# run_speed: returns the dogs running speed (weight/age *10).
# fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speedweight* should win.
# Create 3 dogs and use some of your methods


# Exercise 2 : Dogs Domesticated

# Create a new python file and import your Dog class from the previous exercise.
# Create a class named PetDog that inherits from Dog.
# Add the attribute trained (boolean) to the PetDog class, should always start False
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
# play: gets parameter of any amount of other dogs (look up args) and prints “the dogs: dog_names play together” each of the dogs that plays has their trained boolean switched to False
# do_a_trick: will print one of the following sentences randomly ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
# “dog_name does a barrel roll”
# “dog_name stands on their back legs”
# “dog_name shakes your hand”
# “dog_name plays dead”

class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight 
    def bark(self):
        print("bark bark!")
    def run_speed(self):
        speed = (self.weight/age*10 )
        return speed
    def fight(self):
        bob.fight(bob0)



bob=Dog("bob", 2, 5)
bob0=Dog("bob0", 2, 10)
bob1=Dog("bob1", 2,20)

print(bob)

#fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speedweight* should win.
#dont know 








