# Write a program that takes a person's name
# and outputs a random name for a band

#Instructions: Type your name and start your band.

import sys
import random

def main(args):
	'''
	This program will choose a random band name for you
	based on your name '''
	
	# main loop to repeat the task
	titles = ["gigantic", "huge", "miniscule", "meme",
	          "blue", "small", "aggressive", "eggy", "skinny",
	          "phat", "obese", "crazy"]
	adjs = ["truthful", "abandoned", "adorable", "spirited",
	        "salty", "silky", "hungry", "scratchy", "nerdy",
	        "velvety", "filthy", "zesty", "tasty"]
	pl_nouns = ["penguins", "bats", "cities", "bombs", "giraffes",
	            "zebras", "nuts", "cell phones", "monkeys",
	            "elephants", "llamas", "calves", "obamas"]
	while True:
		name = raw_input("Enter your name: ")
		# randomly choose a title for the persons name
		title = random.choice(titles)
		# randomly choose an adjective to describe the band
		adj = random.choice(adjs)
		# randomly choose a plural noun to name the band
		pl_noun = random.choice(pl_nouns)
		
		print title, name, "and the", adj, pl_noun

if __name__ == "__main__":
	main(sys.argv)