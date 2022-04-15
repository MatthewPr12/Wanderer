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


class Character:
    def __init__(self, name, description, conversation=None):
        self.name = name
        self.description = description
        self.conversation = conversation or ''

    def set_conversation(self, text):
        """
        set the words for the character
        :param text:
        :return:
        """
        self.conversation = text

    def describe(self):
        """
        show main info about the character
        :return:
        """
        typ = type(self).__name__
        print(f"{typ}: {self.name}",
              f"Description: {self.description}", sep='\n')

    def talk(self):
        """
        talk to the character
        :return:
        """
        print(self.conversation)


class Enemy(Character):
    defeated = 0

    def __init__(self, name, description, conversation=None, weakness=None):
        super().__init__(name, description, conversation)
        self.weakness = weakness or ''

    def set_weakness(self, weak):
        """
        define what can enemy be killed with
        :param weak:
        :return:
        """
        self.weakness = weak

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


class Friend(Character):
    def __init__(self, name, description, conversation=None, secret_gift=None):
        super().__init__(name, description, conversation)
        self.secret_gift = secret_gift

    def coffee_time(self):
        print("Let's go to the coffee house. You get to choose one",
              "1) coffee manufactory",
              "2) Lviv coffee mine",
              "3) Aroma Kava", sep='\n')
        choice = input("Enter a number: ")
        if choice in {"1", "2"}:
            print("Good choice")
            if self.secret_gift:
                print("Now I present to you the gift",
                      "that will help you fight the boss")
                return 0
            return 1
        elif choice == "3":
            print("We're not friends anymore.",
                  "Now I have to kill you for your tastes, pervert...")
            return 2
        print("Ugh, sorry, we don't go there. Bye")
        return 3


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


class Boss(Enemy):
    def __init__(self, name, description, conversation):
        super().__init__(name, description, conversation)
        self.name = 'Russian-speaking baron'
        self.description = 'extremely impudent creature'
        self.weakness = 'Iryna Farion'
        self.conversation = "We have a free country. What's the difference?"
