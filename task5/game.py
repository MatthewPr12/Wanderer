"""
module with internal organization of the game
"""


class Room:
    """
    Room class
    """

    def __init__(self, name, description=None, linked_room=None, character=None, item=None):
        """
        constructor
        :param name:
        :param description:
        :param linked_room:
        :param character:
        :param item:
        """
        self.name = name
        self.description = description
        self.linked_room = linked_room or {}
        self.character = character or None
        self.item = item or None

    def __repr__(self):
        """
        dunder method repr
        :return:
        """
        return f"{self.name}\n--------------------\n" \
               f"{self.description}"

    def set_description(self, text):
        """
        provide description for the room
        :param text:
        :return:
        """
        self.description = text

    def link_room(self, other, direction):
        """
        link the room with another one to create
        an integral map
        :param other:
        :param direction:
        :return:
        """
        self.linked_room[direction] = other

    def set_character(self, char):
        """
        set the character that waits for the player in the room
        :param char:
        :return:
        """
        self.character = char

    def set_item(self, item):
        """
        set the item that the player can take
        while visiting the room
        :param item:
        :return:
        """
        self.item = item

    def get_details(self):
        """
        provide player with important information
        about the room
        :return:
        """
        linked = list(self.linked_room.values())[0].name + \
                 ' to the ' + list(self.linked_room.keys())[0] \
            if self.linked_room else 'None'
        char = type(self.character).__name__ + "===" + self.character.name \
            if self.character else 'None'
        item = self.item.name if self.item else None

        print(f"Name: {self.name}", f"Description: {self.description}",
              f"Linked room: {linked}",
              f"Character: {char}",
              f"Item: {item}", sep='\n')

    def move(self, command):
        """
        move to linked room
        :param command:
        :return:
        """
        if command in self.linked_room:
            return self.linked_room[command]
        print("Can't go in such direction")
        return self

    def get_character(self):
        """
        see what character is hiding in the room
        :return:
        """
        return self.character

    def get_item(self):
        """
        get the item that is placed in the room
        :return:
        """
        return self.item


class Enemy:
    """
    Enemy class
    """
    defeated = 0

    def __init__(self, name, description, conversation=None, weakness=None):
        """
        constructor
        :param name:
        :param description:
        :param conversation:
        :param weakness:
        """
        self.name = name
        self.description = description
        self.conversation = conversation or ''
        self.weakness = weakness or ''

    def set_conversation(self, text):
        """
        set the words for the enemy
        :param text:
        :return:
        """
        self.conversation = text

    def set_weakness(self, weak):
        """
        define what can enemy be killed with
        :param weak:
        :return:
        """
        self.weakness = weak

    def describe(self):
        """
        show main info about the enemy
        :return:
        """
        typ = type(self).__name__
        print(f"{typ}: {self.name}",
              f"Description: {self.description}", sep='\n')

    def talk(self):
        """
        talk to the enemy
        :return:
        """
        print(self.conversation)

    def fight(self, fight_with):
        """
        fight with the enemy providing you
        got some proper tools
        :param fight_with:
        :return:
        """
        if fight_with == self.weakness:
            return True
        return False

    def get_defeated(self):
        """
        command for enemy to die. keep the record
        of killed enemies
        :return:
        """
        Enemy.defeated += 1
        return Enemy.defeated


class Item:
    """
    Item class
    """

    def __init__(self, name, description=None):
        """
        constructor
        :param name:
        :param description:
        """
        self.name = name
        self.description = description or ''

    def set_description(self, text):
        """
        provide the item with main info about it
        :param text:
        :return:
        """
        self.description = text

    def describe(self):
        """
        get the main info of the item
        :return:
        """
        typ = type(self).__name__
        print(f"{typ}: {self.name}",
              f"Description: {self.description}", sep='\n')

    def get_name(self):
        """
        get the name of the item
        :return:
        """
        return self.name


class Player:
    """
    player class
    """


class Friend:
    """
    Friend class
    """
