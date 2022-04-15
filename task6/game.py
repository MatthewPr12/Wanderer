class Street:
    def __init__(self, name, description=None, linked_str=None, character=None, item=None):
        self.name = name
        self.description = description
        self.linked_str = linked_str or {}
        self.character = character or None
        self.item = item or []

    def set_description(self, text):
        """
        provide description for the street
        :param text:
        :return:
        """
        self.description = text

    def link_str(self, other, direction):
        """
        link the street with another one to create
        an integral map
        :param other:
        :param direction:
        :return:
        """
        self.linked_room[direction] = other

    def set_character(self, char):
        """
        set the character that waits for the player on the street
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

    def move(self, direction):
        """
        move to linked street
        :param command:
        :return:
        """
        if direction in self.linked_str:
            return self.linked_str[direction]
        print("Can't go in such direction")
        return self

    def get_character(self):
        """
        see what character is hiding on the street
        :return:
        """
        return self.character

    def get_item(self):
        """
        get the item that is placed on the street
        :return:
        """
        return self.item

    


class Enemy:
    pass


class Friend:
    pass


class Character:
    pass
