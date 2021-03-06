import turtle
import random

#Stats for various objects in the game
#sorted by [HP, Attack, Defense, Speed, Luck]
player = [100, 0, 15, 30, 5]
rat = [30,10,5,20,5]

game_screen = turtle.Screen()
game_screen.screensize(1000,1000)
game_screen.setworldcoordinates(0,0,1000,1000)

def intro():
	intro = turtle.Turtle()
	intro.hideturtle()
	intro.penup()
	intro.speed(10)
	intro.goto(500,700)
	intro.write("SOME GENERIC RPG TITLE", False, "center", ("Ariel", 30, "normal"))
	intro.goto(500,600)
	intro.write("A journey of modest porportions", False, "center", ("Ariel", 20, "normal"))
	intro.goto(500,400)
	intro.write("Type start to begin", False, "center", ("Ariel", 20, "normal"))


def start_room():
	narative = turtle.Turtle()
	narative.ht()
	narative.penup()
	narative.speed(10)
	narative.goto(500,600)
	narative.write("You wake up in the dark. Confused and with a headache, you look around trying to get an idea where you are.", False, "center", ("Ariel",12,"normal"))
	narative.goto(500,500)
	narative.write("Suddenly a light appeared from above, shining down the center of the room upon three weapons. A sword, bow and staff.", False, "center", ("Ariel",12,"normal"))
	narative.goto(500,400)
	narative.write("Make your choice", False, "center", ("Ariel",12,"normal"))
	valid_weapon = False
	while valid_weapon == False:
		weapon = input("type in which weapon you want to use ")
		weapon = weapon.upper()
		if weapon == "SWORD" or weapon == "BOW" or weapon == "STAFF":
			valid_weapon = True
			return weapon
	


def fight_rat(player, rat):
	win = False
	

	while win == False:
		rat_new_speed = rat[3] * random.random()
		player_new_speed = player[3] * random.random()
		if rat_new_speed > player_new_speed:
			rat_attack = int(rat[1] * (random.randrange(8,10)*0.1))
			player[0] = player[0] - rat_attack
			print("Rat bites you for " + str(rat_attack) + " damage \n")
			print("you have " + str(player[0]) + " health left \n")
		else:
			attack_type = input("will you want to perform a light or heavy attack? (type light or heavy) ")
			attack_type = attack_type.upper()
			if attack_type == "LIGHT":
				player_attack = int(player[1] * (random.randrange(6,7)*0.1))
				player[3] = player[3] + 5
				rat[0] = rat[0] - player_attack
				print("you hit the rat for " + str(player_attack) + " damage \n")
				if rat[0] <= 0:
					print("You defeated the rat! \n")
					win = True

			elif attack_type == "HEAVY":
				player_attack = int(player[1] * (random.randrange(7,10)*0.1))
				player[3] = player[3] - 8
				rat[0] = rat[0] - player_attack
				print("you hit the rat for " + str(player_attack) + " damage \n")
				if rat[0] <= 0:
					print("You defeated the rat! \n")
					win = True
	return win

def room2():
	narative = turtle.Turtle()
	narative.ht()
	narative.penup()
	narative.speed(10)
	narative.goto(500,600)
	narative.write("You exit through the only door into another dark room. This one has an ominouse feel to it.", False, "center", ("Ariel",12,"normal"))
	narative.goto(500,550)
	narative.write("At the corner of the room, you see a pair of glowing yellow eyes. Startled you take a step back.", False, "center", ("Ariel",12,"normal"))
	narative.goto(500,500)
	narative.write("The eyes took notice and without hesitation, charges at you. It's a rat! You ready your weapon and begin a fight!", False, "center", ("Ariel",12,"normal"))
	print("You start the fight with 100 hit points. If your hitpoints reaches 0, you lose \n")
	action = input("Will you fight or run? ")
	action = action.upper()
	if action == "RUN":
		print("Haha. You thought you had a choice, but you don't \n")
	cont = fight_rat(player,rat)
	if cont:
		game_screen.clearscreen()
		narative.goto(500,600)
		narative.write("You deal the final blow to the rat, and it explodes in a fiery blaze.", False, "center", ("Ariel",12,"normal"))
		narative.goto(500,550)
		narative.write("After settling down and realising you have to find a way out, 3 doors lie before you", False, "center", ("Ariel",12,"normal"))
		narative.goto(500,500)
		narative.write("To the north, you hear growls, as if your fight has brought attention from the other side of the door", False, "center", ("Ariel",12,"normal"))
		narative.goto(500,450)
		narative.write("To the west, you can feel a cold breeze from the next room", False, "center", ("Ariel",12,"normal"))
		narative.goto(500,400)
		narative.write("To the east, compelte silence. Which room do you choose to go to?", False, "center", ("Ariel",12,"normal"))
		next_room = input("Choose which room (north, east or west) to go to ")
		next_room = next_room.upper()
		if next_room == "NORTH":
			return 5
		elif next_room == "WEST":
			return 3
		else:
			return 4


def room3():
	game_screen.clearscreen()

def room4():
	game_screen.clearscreen()

def room5():
	game_screen.clearscreen()


def main():
	intro()
	start = "NONE"
	while start == "NONE":
		start = input("Type start to begin or exit to end the game ")
		start = start.upper()
		if start == "END":
			game_screen.exitonclick()
		elif start == "START":
			game_screen.clearscreen()
			weapon = start_room()
			if weapon == "SWORD":
				player[1] = player[1] + 10
				player[2] = player[2] + 2
				print("You choose a sword \n")
				game_screen.clearscreen()
		
			elif weapon == "BOW":
				player[1] = player[1] + 8
				player[4] = player[4] + 5
				print("You choose a bow \n")
				game_screen.clearscreen()
			
			elif weapon == "STAFF":
				player[1] = player[1] + 12
				player[2] = player[2] - 2
				print("You choose a staff \n")
				game_screen.clearscreen()
		else:
			print("Invalid input!")
			start = "NONE"
			
	next_room = room2()
	if next_room == 3:
		room3()
	elif next_room == 4:
		room4()
	else:
		room5()
	
	game_screen.exitonclick()


main()
