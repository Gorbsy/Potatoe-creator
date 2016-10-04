import random

#dice time

def d2 () :
	return random.randint(1,2)

def d3 () :
	return random.randint(1,3)

def d4 () :
	return random.randint(1,4)

def d6 (count) :
	somme = 0 
	for _ in range(count):
		somme = somme + random.randint(1,6)
	return somme


def d8 () :
	return random.randint(1,8)

def d10 () :
	return random.randint(1,10)

def d12 () :
	return random.randint(1,12)

def d20 () :
	return random.randint(1,20)

def afficher(arg):
	print arg

dc=4
strength = d6(dc)
dexterity = d6(dc)
constitution = d6(dc)
intelligence = d6(dc)
wisdom = d6(dc)
charisma = d6(dc)

print "lets define your characteristics"

print "your strength is ", strength
print "your dexterity is ", dexterity
print "your constitution is ", constitution
print "your intelligence is ", intelligence
print "your wisdom is ", wisdom
print "your charisma is ", charisma

race = raw_input ("what race do you want to play? ")
print "Your character is a ", race


dice = int (raw_input ("how many dice do you want to throw? "))

