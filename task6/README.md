# Wanderer
## Purpose
To win you have to kill **at lest 2** enemies and a boss


## Main Loop
In the beginning of a game a player is given **3 lives** and an empty backpack.
The map is already set.

As the main loop starts the player sees the number of the lives he has, 
the main information about the street where he is, and what he can find on this street
*(Friend, Enemy, Item)*

Starting from this moment the following commands are available for the player:
1) north
2) south
3) east
4) west
5) talk
6) fight
7) take
8) coffee time

### Directions(north, south, east, west)
After entering such commands the player changes his current location to
the street which is placed in the given direction *(if the direction is available. Otherwise, the player will be
notified that he cannot go in the direction)*

### talk
If there is a character on the street(either a friend or an enemy) the player
can talk with one. If there is no-one on the street and the player is trying
to talk then he's gotta visit a doctor)))

### fight
The player can fight the enemy providing s/he has proper tools *(tools needed to kill an enemy are given)*.
After you chose **fight** option you are asked what weapon you want
to use in order to fight the enemy. If you don't have this tool in your backpack
or this tool does not kill your enemy, you lose one life. In the opposite case, you kill the
enemy and the game keeps record of the number of enemies you killed.

**ATTENTION!**

There is one boss in the game that you have to kill in order
to win the game. It can be killed only with the **special secret tool**
which you can get only from your one of your friends. Therefore, you should be polite with them


### take
After entering this command you take the item to your backpack(if it's weapon-type)
or you use it to increase the number of lives you have(if it's support-type)
If there's no item on the street you can't take one

### coffee time
You can have coffee in the coffee house only with the friend. You also get to choose
the coffee house. But **be careful**. Lviv residents tolerate only
good coffee houses. So if you choose a bad one you will be **killed**.
But if you choose a good one, maybe you'll receive a surprise.



