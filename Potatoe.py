import random

#dice time

def d2 (count) :
	somme = 0 
	for _ in range(count):
		somme = somme + random.randint(1,2)
	return somme

def d3 (count) :
	somme = 0 
	for _ in range(count):
		somme = somme + random.randint(1,3)
	return somme

def d4 (count) :
	somme = 0 
	for _ in range(count):
		somme = somme + random.randint(1,4)
	return somme

def d6 (count) :
	somme = 0 
	for _ in range(count):
		somme = somme + random.randint(1,6)
	return somme


def d8 (count) :
	somme = 0 
	for _ in range(count):
		somme = somme + random.randint(1,8)
	return somme

def d10 (count) :
	somme = 0 
	for _ in range(count):
		somme = somme + random.randint(1,10)
	return somme

def d12 (count) :
	somme = 0 
	for _ in range(count):
		somme = somme + random.randint(1,12)
	return somme

def d20 (count) :
	somme = 0 
	for _ in range(count):
		somme = somme + random.randint(1,20)
	return somme

def afficher(arg):
	print arg

dc=4
abilities = {}
abilities["Strength"] = d6(dc), 
abilities["Dexterity"] = d6(dc)
abilities["Constitution"] = d6(dc)
abilities["Intelligence"] = d6(dc)
abilities["Wisdom"] = d6(dc)
abilities["Charisma"] = d6(dc)


modifier = {}
modifier["Strength"] = (abilities["Strength"]/2) - 5



modif = (ability/2) - 5

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


