from game import Street, Enemy, Friend, Item, Boss

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

    syrnyk = Item("syrnyk")
    syrnyk.set_description("God made it and gave to Lviv residents as a gift")
    krakiv.set_item(syrnyk)

    math = Item("math")
    math.set_description("Unbearable for stupid minds")
    kozelnytska.set_item(math)

    beer = Item("beer")
    beer.set_description("Lvivske Rizdviane hits different")
    franka.set_item(beer)

    credit_card = Item("credit card")
    credit_card.set_description("something unknown for russians")

    elixir_of_life = Item("Pyrohy & Pliatsky")
    elixir_of_life.set_description("This healing food resurrected Galicians")
    sheva.set_item(elixir_of_life)

    lives = 3
    backpack = []
    




