class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self._name = char_name
        self.__description = char_description
        self.__conversation = None

    # Describe this character
    def describe(self):
        print( self._name + " is here!" )
        print( self.__description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.__conversation = conversation

    # Talk to this character
    def talk(self):
        if self.__conversation is not None:
            print("[" + self._name + " says]: " + self.__conversation)
        else:
            print(self._name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self._name + " doesn't want to fight with you")
        return True

#inheritance
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.__weakness = None

    def set_weakness(self, weakness):
        self.__weakness = weakness

    def get_weakness(self):
        return self.__weakness

    # Fight with this Enemy
    def fight(self, combat_item):
        if combat_item == self.__weakness:
            print("You fend " + self._name + " off with the " + combat_item )
            return True
        else:
            print(self._name + " crushes you, puny adventurer")
            return False

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

