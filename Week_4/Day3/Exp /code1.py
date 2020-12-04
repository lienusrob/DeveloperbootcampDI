# Exercise 3: Zara
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: France -> blue, Spain -> red, US -> pink, green 
# Create a dictionary called brand, and translate the information above into keys and values.
# Change the number of stores to 2.
# Print a sentence that explains who the clients of Zara are.
# Add a key called country_creation with a value of Spain to brand
# If the key international_competitors is in the dictionary, add the store Desigual.
# Delete the information about the date of creation.
# Print the last international competitor.
# Print in a sentence, the major clothes’ colors in the US.
# Print the amount of key value pairs (length of the dictionary).
# Print only the keys of the dictionary.
# Create another dictionary called more_on_zara with the following information:

brand = {
 	'name': 'Zara',
	'creation_date': 1975,
	'creator_name': 'Amancio Ortega Gaona',
	'type_of_clothes': ['men', 'women', 'children', 'home'],
	'international_competitors': ['Gap', 'H&M', 'Benetton'],
	'number_stores': 7000,
	'major_color': {
	'France': 'blue',
	'Spain': 'red',
	'US': ['pink', 'green']
}
}
brand["country_creation"]="Spain"
brand["international_competitors"].append("Desigual")
print(brand["international_competitors"][-1])

print("the major colors of cloth in the us are" )
print(brand["US"][0,1])
