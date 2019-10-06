## 100yardrunCPX
100 Yard Run is a NeoPixel based Football Game for the Circuit Playground Express (CPX) board based on CircuitPython.  It was inspired by the classic handheld Mattel football Light Emitting Diode (LED) game first released by Mattel around 1977 with a slight twist based based on the CPX NeoPixel layout.  I created 100 Yard Run to show beginner CircuityPython coders how you can create fun games with just NeoPixels and CircuitPython.  The original Mattel football game has a grid of 3 x 9 LEDs where you can move your LED player up and down as well as left and right to avoid the opposing players.  With just 10 NeoPixels available on the CPX I had to be a little creative mapping a football to the CPX.

## To Load Game on CPX:
- Make sure to load Circuity Python 4.1.0 on your CPX before renaming the 100YardRunCPX.py file to code.py that automatically loads the game when you apply power to your CPX. You can download the .UF2 file by clicking on (https://github.com/adafruit/circuitpython/releases/download/4.1.0/adafruit-circuitpython-circuitplayground_express-en_US-4.1.0.uf2).  To figure out how to update your CPX with Circuit Python 4.1.0 please read the Adafruit guide at (https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart)
- Copy the CircuitPython game filename (../code_100YardRun_4pt1.py) as well as all the .wav sound files onto the CPX and rename the game filename to code.py or main.py
- Touch Pin A4 and Pin A3 to move the player left and right as well as move forward (your player will automatically move up once you have gained 20 yards (default code setting) without getting tackled)
- If you have our CPX Button Shield you can comment out the touch pin portion of the code and uncomment the CPX button shield button input code (you could use the two buttons (Button A and Button B) on the CPX but your hands partially block the NeoPixels and takes away from the gameplay)
- Read through Summary of Gameplay before playing game
- Have fun experimenting and changing the difficulty of the game.

## Summary of Gameplay:
- You must run (pushing left button and right buttons) at least 100 times (corresponding to running 100 yards to mimic gameplay in American Football) while avoiding defensive players to get a touchdown (if you get a touchdown the game is over and you win within a certain amount of time)
- How fast you get a touchdown can be used to rank different players in a classroom to add competitive fun to the game having participants compete against each other (this information can be tracked through the mu display area...eventually this could be transmitted via the bluetooth accessory)
- You have a certain amount of time (currently programmed to be 10 seconds) to run 25 yards (if you don't advance 25 yards during this time the game is over) - referee whistle with delay of game penalty
- Every time you get 10 yards you get a first down sound indicated by the referee
- If you collide with one of the defensive players you lose the game (tackle sound and referee whistle)
- Pressing the left or right button advances you down the field by 1 yard
- The game starts as soon as you hit a button   

## Overview of Gameplay:  
- The 100 Yard Run Football Game is designed around a football player that has to dodge other players that are coming down the field from two different sides of the CPX board.
- The mechanics of the game were inspired by the Timberman mobile app game (check out the game to understand the mechanics).  Rather than cutting down a tree and avoiding the branches,  you are instead running down a football field while avoiding opposing football players.  Just like the Timberman game, you dictate how fast the opposing players are coming down the field based on how fast you press the left and right buttons on the CPX Button Shield (or touching the pins if you don't have the shield).  
- The faster you move from left to right the faster the opposing football players are approaching you.  You can't move too slow or you will run out of time before getting at least a certain amount of yards.  
- Since the game is centered around NeoPixels, you can create a variety of colors for the football players.  There are various programming CircuitPython coding features associated with the game that will be eventually be explored.  
(1) Basic multi-tasking concepts for fun gameplay
(2) Leveraging the mixing of music and sound effects to enhance game play
(3) Being able to configure the game to increase the level of difficulty
(4) Extending the basic gameplay to another type of storyline
(5) Adding cardboard accessories to make touch buttons to add to the the game fun
