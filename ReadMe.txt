Despite its many files, the code is mainly organized into 3 game modes, one main driver, and several other classes that just define data structures.

The first game mode is cutscene mode. This effectively acts as a slideshow with narration. It shows an image for a given length of time and plays the accompanying wav file. Cutscenes are also skippable by clicking through the scene.

The second is a movie scene mode. This plays an mpeg1 movie with mp3 sound until the movie is over. Movies are not skippable.

The main mode is the room exploration mode. Rooms have both exits and hotspots. Exits just move you from room to room (and the term room is used very loosely, a different room could be just a different angle), while hotspots play a sound.

Hotspots are also handled in the mouse_button_up() handler because they can have effects like changing global flags. 

Room data is imported via the Rooms CSV file while data affected by global variables is handled either when loading the room or when handling events depending on whether it reads from or writes to the globals. 

To play the game, you just have to click on things. The arrows will lead you from room to room while certain hotspots in each area will also affect things, so click whatever looks interesting. I recommend the cookie. Cookies are delicious.

Credits:

Main Menu:
Eternal Memory - MoVoX
Distributed under the Creative Commons License (http://creativecommons.org/licenses/by/3.0/)

Footsteps and water sound effects: freesfx
http://www.freesfx.co.uk

Makeup: Robin Gardner