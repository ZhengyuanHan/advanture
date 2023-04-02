advanture

CS515-A Project1

Name: Zhengyuan Han

Stevens Email: zhan24@stevens.edu

CWID: 20011343

GitHub URL: https://github.com/ZhengyuanHan/advanture.git

I spent about 9 hours on the project.

I tested my code by using different commands-including baseline, extensions, and undefined commands-, with different formats-including whitespace inside or case-. I also concerned if the game can play, or we can say, if the winning and losing condition works.

bugs and issues:

1. I have no idea about why checking EOF and continue loop function performances diffierent between IDE and terminal.
2. I want the game still works when user input many whitespaces between give/get/drop commmand and item name. However, when I try to use regular expression, I find that regular expression does not allow infinity marks like * or + in look behind.

difficult issue I've solved:

1. Using regular expression to parse users' input to make case and arbitrary whitespace does npt effect the command.
2. Create a desc_backup list in map to allow users' actions sometimes chang the room's description.

extensions:

1. Locked doors: Some rooms are locked,when players try to enter a locked room, they will recieve 'The direction is locked, you should find the key first.', so players should hold keys to unlock the room. Just make sure the key inside plyers' inventory is OK.
2. Winning and losing condition: The game's aim is to use correct battery to fix a power system, when players hold 'h size battery' in invertory and enter the power room, they will win and quit the game. Else, holding wrong size battery and holding no battery will recieve different lossing feedback and quit the game.
3. NPC interaction: I put npcs in some rooms, game will tell players when they enter the room or each time they use 'look' command. Players can use 'talk' command to talk to them, or use 'give [item name]' command to give specific things to npcs for trading. The game will issues an error message to tell players that they can't talk to nobody or give unnecessary item to npcs.
4. All extensions can take effect by reading my own mapfile: asset.map, without effecting the baseline and the original loop.map.
