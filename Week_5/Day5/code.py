import random 

def play():
	user = input ("rock press 'r', paper press'p' scissors press 's'\n")
	user = user.lower()

	computer = random.choice(["r", "p","s"])

	if user == computer: 
		return "its a tie, you have both choosen{}"

	if win(user, computer): 
		return" you have won, you have choosen{}the computer has choosen {}"
	return"you have lost , you have choosen{}the computer has choosen {}"

def win(player, opponent): 
	if (player == "r" and opponent == "s") or (player =="p" and opponent == "r") or (player == "s" and opponent=="p"):
		#return " you have won, you have choosen {}  the computer has choosen {}"
		return True 
	return False 

if __name__ == "__main__":
	print(play())


def multiply(a, b):
    a * b