import random

def d6 () :
	return random.randint(1,6)

race = raw_input ("what race do you want to play? ")
print "Your character is a ", race

somme = 0 

dice = int (raw_input ("how many dice do you want to throw? "))

for _ in range(dice):
	somme = somme + d6()
print somme
