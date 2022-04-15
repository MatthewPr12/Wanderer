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

    




