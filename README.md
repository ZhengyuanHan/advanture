advanture

CS515-A Project1

Name: Zhengyuan Han

Stevens Email: zhan24@stevens.edu

CWID: 20011343

GitHub URL: 

I spent about 9 hours on the project.

I tested my code by using different commands-including baseline, extensions, and undefined commands-, with different formats-including whitespace inside or case-. I also concerned if the game can play, or we can say, if the winning and losing condition works.

bugs and issues:

1. I have no idea about continue receiving users' input if the program faces EOF.
2. I want the game still works when user input many whitespaces between give/get/drop commmand and item name. However, when I try to use regular expression, I find that regular expression does not allow infinity marks like * or + in look behind.

difficult issue I've solved:

1. Using regular expression to parse users' input to make case and arbitrary whitespace does npt effect the command.
2. Create a desc_backup list in map to allow users' verb sometimes chang the room's description.

