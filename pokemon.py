# codecademy Pokemon project
# I want it to be a vs game for two players on the console
# Select 3 pokemon, with a budget of level points
# When a pokeon faints, choose another available pokemon

from random import randint

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
			# Creating dictionary {counter:[Attack,damage]}
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

	# attack_number=int, opponent=pokemon
	def use_attack(self, attack_number, opponent):
		attack = self.attack_list[attack_number][0]
		print("\n{name} used {attack_name}".format(name=self.name, attack_name=attack.name))
		if randint(0,2)==1:
			print("The attack missed!")
			print("{name} still has {health}  hp.\n".format(name=opponent.name, health=str(opponent.current_health)))
		else:
			damage = int(self.attack_list[attack_number][1] * (super_effective(attack.element, opponent.element)))
			opponent.lose_health(damage)


class Attack:
	#name=str, damage=int, element=str Normal, Fire, Water, grass
	def __init__(self, name, damage, element="Normal"):
		self.name=name
		self.damage=damage
		self.element=element

player_list=[]
class Player:
	def __init__(self, name, pokemon):
		self.name=name
		self.pokemon=pokemon
		player_list.append(self)


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

tackle=Attack("Tackle", 5)
flamethrower=Attack("Flamethrower", 10, "Fire")
bubble=Attack("Bubble",10,"Water")
leaf=Attack("Leaf Throw",10,"Grass")
throw=Attack("Throw", 10)

charmander=Pokemon("Charmander",4,"Fire",[tackle,flamethrower])
squirtle=Pokemon("Squirtle",5,"Water",[tackle,bubble])
bulbasaur=Pokemon("Bulbasaur",7,"Grass",[tackle,leaf])
geodude=Pokemon("Geodude",6,"Rock",[tackle,throw])

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
print()

# player=Player, opponent=Player
def turn(player, opponent):
	print(player.name+"'s turn!")
	print(player.pokemon.name)
	for i in player.pokemon.attack_list:
		print("{number}: {attack_name} - {damage}hp".format(\
			number = str(i),\
			attack_name = player.pokemon.attack_list[i][0].name,\
			damage = str(player.pokemon.attack_list[i][1])))
	attack_number=int(input("Choose attack number: "))
	player.pokemon.use_attack(attack_number, opponent.pokemon)



while (player1.pokemon.faint == False) and (player2.pokemon.faint == False):
	turn(player1,player2)
	if player2.pokemon.faint == True:
		break
	turn(player2,player1)


# Endgame
print()
if player1.pokemon.faint==True:
	print(player2.name + " wins with " + player2.pokemon.name + "!!!")
else:
	print(player1.name + " wins with " + player1.pokemon.name + "!!!")


