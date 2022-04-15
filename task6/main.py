from game import Street, Enemy, Friend, Weapon, Boss, Support
def check_conditions(conditions):
    for i in conditions:
        if not conditions[i]:
            return False
    return True


def main():
    stryyska = Street("Stryyska")
    stryyska.set_description("One of the longest roads in Lviv(7.5 km)")

    kozelnytska = Street("Kozelnytska")
    kozelnytska.set_description("There's one great uni on this street")

    franka = Street("Ivana Franka")
    franka.set_description("Named after famous Lviv writer")

    sheva = Street("Taras Shevchenko avenue")
    sheva.set_description("You know, who Shevchenko is, right?")

    krakiv = Street("Krakivska")
    krakiv.set_description("Sounds like the name of Polish city. And not by accident")

    svoboda = Street("Svoboda Avenue")
    svoboda.set_description("main street of Lviv")

    stryyska.link_str(kozelnytska, 'east')
    kozelnytska.link_str(stryyska, 'west')

    kozelnytska.link_str(franka, 'north')
    franka.link_str(kozelnytska, 'south')

    franka.link_str(sheva, 'west')
    sheva.link_str(franka, 'east')

    sheva.link_str(krakiv, 'north')
    krakiv.link_str(sheva, 'south')

    krakiv.link_str(svoboda, 'west')
    svoboda.link_str(krakiv, 'east')

    kavaler = Friend('Kavaler Vasyl', 'bought BTC back in 2010',
                     secret_gift='Iryna Farion')
    kavaler.set_conversation("Hi, I've got coffee in my veins")
    svoboda.set_character(kavaler)

    lotr = Enemy("Lotr Piotr", "Scoundrel")
    lotr.set_conversation("I can steal your purse, you won't even notice")
    lotr.set_weakness("syrnyk")
    krakiv.set_character(lotr)

    zbuy = Enemy("Zbuy Leonid", "Local fat bully")
    zbuy.set_conversation("Do you know, what region you're in?")
    zbuy.set_weakness("math")
    stryyska.set_character(zbuy)

    batyar = Enemy("Batyar Ivan", "Got nice tobacco pipe")
    batyar.set_conversation("Wanna take a stroll down the street. I can drive you on tram")
    batyar.set_weakness("beer")
    franka.set_character(batyar)

    laydak = Enemy("Laydak Arkadii", "Lviv is my home, literally")
    laydak.set_conversation("Got a penny?")
    laydak.set_weakness("credit card")
    kozelnytska.set_character(laydak)

    nechyst = Boss()
    sheva.set_character(nechyst)

    syrnyk = Weapon("syrnyk")
    syrnyk.set_description("God made it and gave to Lviv residents as a gift")
    kozelnytska.set_item(syrnyk)

    math = Weapon("math")
    math.set_description("Unbearable for stupid minds")
    krakiv.set_item(math)

    beer = Weapon("beer")
    beer.set_description("Lvivske Rizdviane hits different")
    franka.set_item(beer)

    credit_card = Weapon("credit card")
    credit_card.set_description("something unknown for russians")

    elixir_of_life = Support("Pyrohy & Pliatsky")
    elixir_of_life.set_description("This healing food resurrected Galicians")
    sheva.set_item(elixir_of_life)

    lives = 3
    backpack = []
    curr_street = stryyska
    conditions= {"killed": False, 'boss': False}

    while lives > 0:
        if check_conditions(conditions):
            print("Congratulations!!! Armed Forces of Ukraine need you")
            quit()

        print('\033[94m' + "LIVES: " + str(lives) + '\033[0m')
        curr_street.get_info()

        resident = curr_street.get_character()
        item = curr_street.get_item()
        if item is not None:
            item.describe()

        if resident is not None:
            resident.describe()

        command = input(">>> ")

        if command in {"north", "south", "east", "west"}:
            # Move in the given direction
            curr_street = curr_street.move(command)

        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            if resident is not None:
                resident.talk()
            else:
                print("Are you having schizophrenia? There's no one here")

        elif command == "fight":
            if resident is not None:
                if isinstance(resident, Friend):
                    print("Why would you fight a friend?")
                elif isinstance(resident, Boss):
                    print("This fight will be LEGENDARY")
                    print("What will you fight with?")
                    fight_with = input(">>> ")
                    if fight_with in backpack:
                        if resident.fight(fight_with):
                            print("Lviv without russian. Dreams do come true")
                            curr_street.character = None
                            print("Congratulations, you have completed one condition to win")
                            conditions['boss'] = True
                        else:
                            print("Oh dear, you lost the fight.")
                            print("It costs you 3 lives")
                            lives -= 3
                    else:
                        print("You don't have a " + fight_with)
                        print("It costs you 3 lives")
                        lives -= 3
                else:
                    print("What will you fight with?")
                    fight_with = input(">>> ")
                    if fight_with in backpack:
                        if resident.fight(fight_with):
                            print("Successful Lviv cleaning. Lviv Territorial Defence is proud of you")
                            curr_street.character = None
                            if resident.get_defeated() == 2:
                                print("Congratulations, you have completed one condition to win")
                                conditions['killed'] = True

                        else:
                            print("Oh dear, you lost the fight.")
                            print("It costs you a life")
                            lives -= 1
                    else:
                        print("You don't have a " + fight_with)
                        print("It costs you a life")
                        lives -= 1
            else:
                print("There's no one here to fight with, shybenyku")
        elif command == "take":
            if item is not None:
                if isinstance(item, Support):
                    lives += 1
                    print("You can now live for 1 life longer")
                else:
                    print("You put the " + item.get_name() + " in your backpack")
                    backpack.append(item.get_name())
                curr_street.set_item(None)
            else:
                print("There's nothing here to take!")
        elif command == "coffee time":
            if resident is not None:
                if isinstance(resident, Friend):
                    choice = resident.coffee_time()
                    if choice == 0:
                        backpack.append(resident.secret_gift)
                    elif choice == 2:
                        lives -= 1

        else:
            print("I don't know how to " + command)
    else:
        print("Life has come to an end my friend")


if __name__ == "__main__":
    main()
