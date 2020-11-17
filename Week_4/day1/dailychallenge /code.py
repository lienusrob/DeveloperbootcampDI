text = input ("enter something with 10 characters")

# if len(text) != 10: 
# 		pring("Not 10 characters")
# 		exit()


# print(text[0], text[-1])

for i in range(len(text)): 
	print(text[0:i+1])