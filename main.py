#libreries
from room import Room
from character import Enemy, Friend
from rpginfo import RPGInfo
from item import Item

#Title of game
spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

#Backpack of player
Backpack = [3]

#Rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

#Number of rooms
print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

#Link Rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

#Items

torch = Item("Torch")
torch.set_description("Useful in dark places")
ballroom.set_item(torch)

cheese = Item("Cheese")
cheese.set_description("smell Horrible")
kitchen.set_item(cheese)

#Enemy
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)


#Friend
steve = Friend("Steve", "Another adventurer")
steve.set_conversation("Hello my name is Steve, Can I help you?")
kitchen.set_character(steve)

current_room = kitchen

life = True
number_of_items = 0

while life:		
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()

    var_item = current_room.get_item()

    if var_item is not None:
        var_item.describe()

    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")

    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
    # Add code here
        inhabitant.talk()

    elif command == "fight":
        if bool(Backpack):
            for step in range(len(Backpack)):
                print(Backpack[step].get_name())

            print("Choose your item")
            command = input("> ")
            life = inhabitant.fight(command)
        else:
            print("You have not items")

    elif command == "take":
        Backpack[number_of_items] = current_room.get_item()
        print("Took the " + var_item.get_name())
        number_of_items = number_of_items + 1

    if life is False:
        print("You lose")

RPGInfo.credits()
