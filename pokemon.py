# codecademy Pokemon project
# I want it to be a vs game for two players on the console
# Select 3 pokemon, with a budget of level points
# When a pokeon faints, choose another available pokemon

pokemon_list=[]

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
			# Creating dictionary {counter:[name,damage]}
			self.attack_list[i+1] = [attacks[i],int(attacks[i].damage*((10+self.level)/10))]
		pokemon_list.append(self)

	def __repr__(self):
		attacks_string=""
		for i in self.attack_list:
			attacks_string += (self.attack_list[i][0].name + " - " + str(self.attack_list[i][1])+" damage\n")

		return("{name}\nLevel: {level}\nElement: {element}\nHealth: {health}\nAttacks: \n{attacks}"
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


	def use_attack(self, attack_number, opponent):
		attack = self.attack_list[attack_number][0]
		damage = int(self.attack_list[attack_number][1] * (super_effective(attack.element, opponent.element)))
		print("\n{name} used {attack_name}".format(name=self.name, attack_name=attack.name))
		opponent.lose_health(damage)


class Attack:
	#name=str, damage=int, element=str Normal, Fire, Water, grass
	def __init__(self, name, damage, element="Normal"):
		self.name=name
		self.damage=damage
		self.element=element

class Player:
	def __init__(self, name, pokemon):
		self.name=name
		self.pokemon=pokemon

# Super Effective function
def super_effective(attack_type, opponent_type):
	if (attack_type == "Water" and opponent_type == "Fire")\
	or (attack_type == "Grass" and opponent_type == "Water")\
	or (attack_type == "Fire" and opponent_type == "Grass"):
		print("It's super effective!")
		return 1.5
	elif (attack_type == "Grass" and opponent_type == "Fire")\
	or (attack_type == "Fire" and opponent_type == "Water")\
	or (attack_type == "Water" and opponent_type == "Grass")\
	or (attack_type == "Normal" and opponent_type == "Rock"):
		print("It's not very effective....")
		return 0.5
	else:
		return 1

tackle=Attack("Tackle", 10)
flamethrower=Attack("Flamethrower", 15, "Fire")
bubble=Attack("Bubble",15,"Water")
leaf=Attack("Leaf Throw",15,"Grass")
throw=Attack("Throw", 15)

charmander=Pokemon("Charmander",4,"Fire",[tackle,flamethrower])
squirtle=Pokemon("Squirtle",5,"Water",[tackle,bubble])
bulbasaur=Pokemon("Bulbasaur",7,"Grass",[tackle,leaf])
geodude=Pokemon("Geodude",11,"Rock",[tackle,throw])

#game start
for pokemon in pokemon_list:
	print(pokemon)

player1_name=input("Player 1: What is your name? ")
print("Which pokemon would you like to use?")
for i in range(len(pokemon_list)):
	print(str(i+1)+": "+pokemon_list[i].name)
player1_choice=input()
player1=Player(player1_name, pokemon_list[int(player1_choice)-1])
print()

player2_name=input("Player 2: What is your name? ")
print("Which pokemon would you like to use?")
for i in range(len(pokemon_list)):
	print(str(i+1)+": "+pokemon_list[i].name)
player2_choice=input()
player2=Player(player2_name, pokemon_list[int(player2_choice)-1])

print()
print(player1.name+" chose "+player1.pokemon.name)
print(player2.name+" chose "+player2.pokemon.name)
print("Let's play!")



#while charmander.faint==False and squirtle.faint==False:
#	print("Charmander's turn!")
#	print()
#	for n in charmander.attack_list:
#		print("{n}: {name} - {damage}hp".format(n=n, name=charmander.attack_list[n][0].name, damage=str(charmander.attack_list[n][1])))
#	print()
#	attack_number=int(input("Which attack number? "))
#
#	charmander.use_attack(attack_number,squirtle)
#	if squirtle.faint==True:
#		break
#
#	print("Squirtle's turn!")
#	print()
#	for n in squirtle.attack_list:
#		print("{n}: {name} - {damage}hp".format(n=n, name=squirtle.attack_list[n][0].name, damage=str(squirtle.attack_list[n][1])))
#	print()
#	attack_number=int(input("Which attack number? "))
#	squirtle.use_attack(attack_number,charmander)
#

#endgame
#if charmander.faint==True:
#	print("Squirtle wins!")
#else:
#	print("Charmander wins!")


