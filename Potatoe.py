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
ability = {}
ability["Strength"] = d6(dc)
ability["Dexterity"] = d6(dc)
ability["Constitution"] = d6(dc)
ability["Intelligence"] = d6(dc)
ability["Wisdom"] = d6(dc)
ability["Charisma"] = d6(dc)

print "lets define your Abilities"

print "Your Abilities now are:"

for key in ability:
	print key, ability[key]

race = raw_input ("what race do you want to play? ")
print "Your character is a ", race

if race == "Elf":
	ability["Dexterity"] += 2
	ability["Constitution"] -= 2

if race == "Dwarf": 
	ability["Constitution"] += 2
	ability["Charisma"] -= 2

if race == "Gnome":
	ability["Constitution"] += 2
	ability["Strength"] -= 2

if race == "Half-orc":
	ability["Strength"] += 2
	ability["Intelligence"] -= 2
	ability["Charisma"] -= 2

if race == "Halfling":
	ability["Dexterity"] += 2
	ability["Strength"] -= 2

if race == "Human":
	pass
if race == "Half-elf":
	pass

print "Your modified Abilities now are:"

for key in ability: 
	print key, ability[key]


