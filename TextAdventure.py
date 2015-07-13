import yaml

cont = True; # Exit condition
stream = file('textadv.yml')
game_data = yaml.load(stream)
current_room = game_data["startroom"]
all_items = game_data["items"]
def showhelp(args=""):
	for command in commands:
		print command + " - " + commands[command][1]
		
def go(direction):
	try:
		global current_room
		next_room = current_room[direction]
		current_room = game_data[next_room]
	except KeyError:
		print "Oops! You can't go that way!"
		return
	describe()
	

def go_north(args=""):
	go("north")
def go_east(args=""):
	go("east")
def go_south(args=""):
	go("south")
def go_west(args=""):
	go("west")
	
def describe(args=""):
	print current_room["name"] + "\n" + current_room["description"] + "\n"
	for item in current_room["items"]:
		print "You see a " + item + " here"
def exit(args=""):
	global cont
	cont = False
def read(args=""):
	if len(args) == 0:
		print "What would you like to read?"
	else:
		get_property("read", args)
def examine(args=""):
	if len(args) == 0:
		print "What would you like to examine?"
	else:
		get_property("examine", args)
def get_property(property, item):

	if item in current_room["items"]:
		try:
			print all_items[item][property]
		except KeyError:
			print "I don't know how to do that!"
	else:
		print "I don't see that here"
def ninjacommand(args=""):
	print "NINJA!"
	
commands = {
"north"   : [go_north, "Walk north!"],
"south"   : [go_south, "Quest south!"],
"east"	  : [go_east, "Stroll east!"],
"west"    : [go_west, "Trot west!"],
"look"    : [describe, "Shows a description of the immediate surroundings!"],
"help"    : [showhelp, "Shows help!"],
"bye"     : [exit, "Closes the program"],
"read"    : [read, "Reads something in the game"],
"examine" : [examine, "Examines an object in the game"]
}

hidden_commands = {
"ninja" : ninjacommand
}

def input():
	input = raw_input("> ")
	cmd = input
	args = ""
	if " " in input:
		cmd = input[:input.index(" ")]
		args = input[input.index(" ") + 1:]
	if cmd in commands:
		commands[cmd][0](args)
	elif cmd in hidden_commands:
		hidden_commands[cmd](args)
	else:
		print "Invalid command!"
describe()
while cont:
	input()
