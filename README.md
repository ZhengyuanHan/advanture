advanture

CS515-A Project1

Name: Zhengyuan Han

Stevens Email: zhan24@stevens.edu

CWID: 20011343

GitHub URL: https://github.com/ZhengyuanHan/advanture.git

I spent about 9 hours on the project.

I tested my code by using different commands-including baseline, extensions, and undefined commands-, with different formats-including whitespace inside or case-. I also concerned if the game can play, or we can say, if the winning and losing condition works.

bugs and issues:

1. I have no idea about continue receiving users' input if the program faces EOF.
2. I want the game still works when user input many whitespaces between give/get/drop commmand and item name. However, when I try to use regular expression, I find that regular expression does not allow infinity marks like * or + in look behind.

difficult issue I've solved:

1. Using regular expression to parse users' input to make case and arbitrary whitespace does npt effect the command.
2. Create a desc_backup list in map to allow users' actions sometimes chang the room's description.

extensions:

1. Drop: Players may drop their holding items wherever they want, but when they drop their item in some specific situations, it will change the description of the room to give players some hints.
2. Winning and losing condition: The game's aim is to find a correct way, so just follow the game and choose you route, if players finally enter the correct terminal, they will win, else, if players enter a wrong terminal, they will lose the game.
3. NPC interaction: I put npcs in some rooms, game will tell players when they enter the room or each time they use 'look' command. Players can use 'talk' command to talk to them, or use 'give' command to give specific things to npcs for trading.
4. Help: When players enter a wrong command, the game will tell them to use 'help' command for help. By using 'help' command, players can also know the background story and what is their final goal in this game.
5. All extensions can take effect by reading my own mapfile: world.map, without effecting the baseline and the original loop.map.
