# codecademy Pokemon project
# I want it to be a vs game for two players on the console
# Pick a trainer that has a list of three pokemon and items
# When a pokeon faints, choose another available pokemon


class Pokemon:
	#name=str, element=str, max_health=int, current_health=int, faint=bool, attacks=[Attack,,,]
	def __init__(self, name, level, element, attacks):
		self.name=name
		self.level=level
		self.element=element
		self.max_health=20 + (5*level)
		self.current_health=self.max_health
		self.faint=False
		self.attacks=attacks
		#Making attack list dependent on level
		self.attack_list={}
		for i in range(len(attacks)):
			self.attack_list[i+1]=[attacks[i],int(attacks[i].damage*((10+self.level)/10))]


	def __repr__(self):
		attacks_string=""
		for i in self.attack_list:
			attacks_string += (self.attack_list[i][0].name + " - " + str(self.attack_list[i][1])+" damage\n")

		return("{name}\nLevel: {level}\nElement: {element}\nHealth: {health}\nAttacks: \n{attacks}\n"
			.format(name=self.name, level=str(self.level), element=self.element, health=str(self.current_health), \
			attacks=attacks_string))
	#damage=int
	def lose_health(self, damage):
		self.current_health-=damage
		if self.current_health<=0:
			self.current_health=0
			self.faint=True
			print("{name} has fainted!".format(name=self.name))
		else:
			print("{name} now has {health} hp.\n".format(name=self.name, health=str(self.current_health)))

	def super_effective(attack_type,opponent_type):
		if (attack_type == "Grass" and opponent_type == "Water")\
		or (attack_type == "Fire" and opponent_type == "Grass")\
		or (attack_type == "Water" and opponent_type == "Fire"):
			return 2
		else:
			return 1

	def use_attack(self, attack_number, opponent):
		print("\n{name} used {attack_name}".format(name=self.name, attack_name=self.attack_list[attack_number][0].name))
		opponent.lose_health(self.attack_list[attack_number][1])

# Trainer class
class Trainer:
	#name=str, poke1/2/3=Pokemon
	def __init__(self, name, poke1, poke2, poke3):
		self.name=name
		self.poke_list={1:poke1,2:poke2,3:poke3}

	def __repr__(self):
		return(self.name+"\n"+self.poke_list)

class Attack:
	#name=str, damage=int, element=str Normal, Fire, Water, grass
	def __init__(self, name, damage, element="Normal"):
		self.name=name
		self.damage=damage
		self.element=element

tackle=Attack("Tackle", 10)
flamethrower=Attack("Flamethrower", 15, "Fire")
bubble=Attack("Bubble",15,"Water")
leaf=Attack("Leaf Throw",15,"Grass")


charmander=Pokemon("Charmander",4,"Fire",[tackle,flamethrower])
squirtle=Pokemon("Squirtle",5,"Water",[tackle,bubble])
bulbasaur=Pokemon("Bulbasaur",7,"Grass",[tackle,leaf])

#Battle function
print(charmander)
print(squirtle)
print(bulbasaur)

while charmander.faint==False and squirtle.faint==False:
	print("Charmander's turn!")
	print()
	for n in charmander.attack_list:
		print("{n}: {name} - {damage}hp".format(n=n, name=charmander.attack_list[n][0].name, damage=str(charmander.attack_list[n][1])))
	print()
	attack_number=int(input("Which attack number? "))
	
	charmander.use_attack(attack_number,squirtle)
	if squirtle.faint==True:
		break

	print("Squirtle's turn!")
	print()
	for n in squirtle.attack_list:
		print("{n}: {name} - {damage}hp".format(n=n, name=squirtle.attack_list[n][0].name, damage=str(squirtle.attack_list[n][1])))
	print()
	attack_number=int(input("Which attack number? "))
	squirtle.use_attack(attack_number,charmander)

# Super effective function:
def super_effective(attack_type,opponent_type):
	if attack_type == "Grass" and opponent_type == "Water"\
	or attack_type == "Fire" and opponent_type == "Grass"\
	or attack_type == "Water" and opponent_type == "Fire":
		return [True,2]
	else:
		return [False,1]

#endgame
if charmander.faint==True:
	print("Squirtle wins!")
else:
	print("Charmander wins!")


