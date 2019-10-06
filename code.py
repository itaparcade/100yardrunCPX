# 100 Yard Run Football Game for Circuit Playground Express(CPX) based on CircuitPython 
# This code has been tested with CircuitPython 4.1
# iTapArcade.com
# Author: Wil Myrick
# Created Date: April 2018
# Last Update: October 6, 2019
# Twitter: @iTapArcade
# Version 2.0: Works with CPX Button Shield Board from iTapArcade 
# Learn -- Build -- Code -- Play
#
# Follow me on Twitter @iTapArcade and let others know about this project!
# Get on the waiting list if interested in purchasing the CPX Button Shield Board (Link Below)
# https://www.tindie.com/products/itaparcade/button-shield-kit-for-circuit-playground-express/ 
# to help keep more free CircuitPython game coding projects like this coming!
#
# TO LOAD GAME ON CPX:
# 1) Make sure to load CircuityPython 4.1 version on the CPX (https://circuitpython.org/board/circuitplayground_express/) before renaming the game filename to code.py 
# 2) Copy the CircuitPython file code.py associated with this game on the CPX
# 3) Press the left or right running buttons on CPX Button Shield to start game
# 4) If you don't have our CPX Button Shield you can touch Pins A4 and A3 on the CPX to still play the game (you could use the two buttons on the CPX but your hands partially block the NeoPixels and takes away from the gameplay)
# 5) Read through Summary of Gameplay before playing game
# 6) Have fun experimenting and changing the difficulty of the game.
#    
# SUMMARY OF GAMEPLAY:
# - You must run (pushing left button and right buttons) at least 100 times (corresponding to running 100 yards to mimic gameplay in American Football) while avoiding defensive players to get a touchdown (if you get a touchdown you beat the game)
# - How fast you get a touchdown can be used to rank different players in a classroom to add competitive fun to the game having participants compete against each other (this information can be tracked through the mu display area...eventually this could be transmitted via the bluetooth acessory)
# - You have a certain amount of time (currently programmed to be 10 seconds) to run 25 yards (if you don't advance 25 yards during this time the game is over) - referee whistle with delay of game penalty will sound
# - Every time you get 10 yards you get a first down sound indicated by the referee sound
# - If you collide with one of the defensive players you lose the game (tackle sound and referee whistle)
# - Pressing the left or right button (or touching Pins A4 or A3) advances you down the field by 1 yard
# - The game starts as soon as you hit a button (or touch Pins A4 or A3)  
#
# OVERVIEW OF GAMEPLAY:  
# - The 100 Yard Run Football Game is designed around a football player that has to dodge other players that are coming down the field from two different sides of the CPX board. 
# - The mechanics of the game were inspired by the Timberman mobile app game (check out the game to understand the mechanics).  Rather than cutting down a tree and avoiding the branches,  you are instead running down a football field while avoiding opposing football players.  Just like the timberman game, you dictate how fast the opposing players are coming down the field based on how fast you press the left and right buttons on the CPX Button Shield.  
# - The faster you move from left to right the faster the opposing football players are approaching you.  You can't move too slow or you will run out of time before getting at least a certain amount of yards.  
# - Since the game is centered around NeoPixels, you can create a variety of colors for the football players.  There are various programming CircuitPython coding features associated with the game.  
# (1) Basic multi-tasking CircuityPython coding concepts for fun gameplay 
# (2) Leveraging the mixing of music and sound effects to enhance gameplay 
# (3) Being able to configure the game to increase the level of difficulty 
# (4) Adding cardboard based touch buttons or arcade buttons for added gameplay 

# Load libraries needed to operate 
import board
import neopixel
import digitalio
import time
import audioio
import random
import touchio

# Setup NeoPixel Display and Fill NeoPixels Green to respresent football field
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0x10,0))

# Enable the speaker to play the various sounds for the game
# It is highly recommended to connect the speaker output to a speaker system to enhance the game play
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

# Mute Switch for Sound
#sound_switch = digitalio.DigitalInOut(board.D7)
#sound_switch.direction = digitalio.Direction.INPUT
#sound_switch.pull = digitalio.Pull.UP

# Beginning of Code Section for Game Input Selection Options
#
# Comment and Uncomment code approriately based on the type of input you want to play the game
# CPX TOUCH INPUT OPTION
# Left Move Touch Option for Offensive Player
button_left_move = touchio.TouchIn(board.A4)
# Right Move Touch Option for Offensive Player
button_right_move = touchio.TouchIn(board.A3)

# CPX BUTTON A and BUTTON B INPUT OPTION
# Left Move CPX Button Option for Offensive Player
#button_left_move = digitalio.DigitalInOut(board.BUTTON_A)
#button_left_move.direction = digitalio.Direction.INPUT
#button_left_move.pull = digitalio.Pull.DOWN
# Right Move CPX Button Option for Offensive Player
#button_right_move = digitalio.DigitalInOut(board.BUTTON_B)
#button_right_move.direction = digitalio.Direction.INPUT
#button_right_move.pull = digitalio.Pull.DOWN

# CPX BUTTON SHIELD INPUT OPTION
# Left Move CPX Button Shield Option for Offensive Player
#button_left_move = digitalio.DigitalInOut(board.A6)
#button_left_move.direction = digitalio.Direction.INPUT
#button_left_move.pull = digitalio.Pull.UP
# Right Move CPX Button Shield Option for Offensive Player
#button_p4 = digitalio.DigitalInOut(board.A1)
#button_p4.direction = digitalio.Direction.INPUT
#button_p4.pull = digitalio.Pull.UP
#
#End of Code Section for Game Input Selection Options


# Beginning of Code Section to Select Colors for Offensive and Defensive Players
#
# Comment and Uncomment code approriately based on the type of colors you want to select for the players
# Define various NeoPixel Colors for Offensive Player, Definsive Players, and Football Field Display
#
# Basic Colors Defined
#RED = 0x100000 # (0x10, 0, 0) also works
#YELLOW=(0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
#AQUA = (0, 0x10, 0x10)
#BLUE = (0, 0, 0x10)
#PURPLE = (0x10, 0, 0x10)
BLACK = (0,0,0)
#
# Some Predefined Football Team Colors 
#CUST = (12,38,76)
#BALTIMORE_TEAM = (36,23,115)
DALLAS_TEAM = (12,38,76)
#DENVER_TEAM = (251,79,20)
#CHICAGO_TEAM = (0,20,63)
#NEW_ENGLAND_TEAM = (200,31,50)
#NEW_YORK_TEAM = (25,46,108)
WASHINGTON_DC_TEAM = (124,20,21)
#LAS_VEGAS_TEAM =(196,201,204)
#PITTSBURGH_TEAM = (255,194,14)
#MINNESOTA_TEAM = (79,46,132)
#TAMBA_BAY_TEAM = (212,9,9)
#HOUSTON_TEAM = (0,20,63)
#DETRIOT_TEAM = (4,110,180)
#LA_TEAM = (253,181,21)
#
# End of Code Section to Select Colors for Offensive and Defensive Players


# Field Location Counter - variable tracks how many yards the player has advanced
total_yards = 0

# Setup states for tracking buttons pressed - these variables are used to lockout buttons once pressed so a player cannot continuosly hold down a button to advance
lockout_left_move = True
lockout_right_move = True

game_board_timer = 1
game_board_time_seconds = 0
previousTime = 0
timer_toggle = True
game_over = True
#game_start = False

# Section of code to change colors of offensive and defensive players
#colors[offense,defense,....,....,field,....,background]
colors=[DALLAS_TEAM,WASHINGTON_DC_TEAM,BLACK,BLACK,GREEN,BLACK,GREEN]
left_board_track = [6,6,6,6,6]
right_board_track = [6,6,6,6,6]


# Determine the number of football yards per row of NeoPixels on CPX
level_2_yards = 25
level_3_yards = 50
level_4_yards = 75
win_game_yards = 100

# Level 1 Game Board Setup
sel_pixels_left = [0,1,2,3]
sel_pixels_right = [0,1,2,3]
left_field_player_pixel = 4
right_field_player_pixel = 5

# Setup and load sound files to be used during the game
audiofiles=["background_music.wav","tackle_sound.wav","firstdown_sound.wav","referee_whistle_sound.wav","delay_of_game_sound.wav","referee_touchdown_sound.wav","crowd_touchdown_sound.wav"]
wave_f1 = audioio.WaveFile(open(audiofiles[0],"rb"))
wave_f2 = audioio.WaveFile(open(audiofiles[1],"rb"))
wave_f3 = audioio.WaveFile(open(audiofiles[2],"rb"))
wave_f4 = audioio.WaveFile(open(audiofiles[3],"rb"))
wave_f5 = audioio.WaveFile(open(audiofiles[4],"rb"))
wave_f6 = audioio.WaveFile(open(audiofiles[5],"rb"))
wave_f7 = audioio.WaveFile(open(audiofiles[6],"rb"))
mixer = audioio.Mixer(voice_count=3, sample_rate=22050, channel_count=1, bits_per_sample=16, samples_signed=True)
audio = audioio.AudioOut(board.SPEAKER) 

#mixer.play(wave_f1, voice=0, loop=True)
#mixer.play(wave_f1, voice=0)

#Function Modules that generate certain states of the game

# Play out of time sound
def OutofTime():
    audio.play(wave_f4)
    time.sleep(1)
    audio.play(wave_f5)   

# Called when player collides with defensive player, game level timer has elapsed, or touchdown
def GameOver():
    global game_board_time_seconds
    global total_yards
    global sel_pixels_left
    global sel_pixels_right
    global left_field_player_pixel
    global right_field_player_pixel
    global left_board_track
    global right_board_track
    global game_over
    mixer.stop_voice(voice=0)
    time.sleep(3)
    game_board_time_seconds = 0
    total_yards = 0
    sel_pixels_left = [0,1,2,3]
    sel_pixels_right = [0,1,2,3]
    left_field_player_pixel = 4
    right_field_player_pixel = 5
    left_board_track = [6,6,6,6,6]
    right_board_track = [6,6,6,6,6]
    game_over = True
    pixels.fill((0,0x10,0))
    
# Called to provide neopixel animation for random white sparkles to indicate touchdown
def sparkles(wait):  # Random sparkles - lights just one NeoPixel at a time
    i = random.randint(0, len(pixels) - 1)  # Choose random pixel
    pixels[i] = (255, 255, 255)  # Set it to current color
    pixels.write()  # Refresh NeoPixel states
    # Set same pixel to "off" color now but DON'T refresh...
    # it stays on for now...bot this and the next random
    # pixel will be refreshed on the next pass.
    pixels[i] = (0, 0, 0)
    time.sleep(wait)  # 8 millisecond delay     

# Called to define second level of game
def Level2():
    global sel_pixels_left
    global sel_pixels_right
    global left_field_player_pixel
    global right_field_player_pixel
    mixer.play(wave_f7, voice=2)
    sel_pixels_left = [0,1,2,4]  # i=2
    sel_pixels_right = [0,1,2,4] # i=2
    left_field_player_pixel = 3  # i+1 = 3
    right_field_player_pixel = 6 # i*2 = 6

# Called to define third level of game
def Level3():
    global sel_pixels_left
    global sel_pixels_right
    global left_field_player_pixel
    global right_field_player_pixel
    mixer.play(wave_f7, voice=2)
    sel_pixels_left = [0,1,3,4]  # i=3
    sel_pixels_right = [0,1,3,4] # i=3
    left_field_player_pixel = 2  # i-1 = 2
    right_field_player_pixel = 7 # 2*i+1 = 7

# Called to define fourth level of game
def Level4():
    global sel_pixels_left
    global sel_pixels_right
    global left_field_player_pixel
    global right_field_player_pixel
    mixer.play(wave_f7, voice=2)
    sel_pixels_left = [0,2,3,4]   #
    sel_pixels_right = [0,2,3,4]
    left_field_player_pixel = 1
    right_field_player_pixel = 8   
    
# Called to mix touchdown and crowd sound effects with sparkle animation to indicate touchdown  
def Flash():
    mixer.play(wave_f6, voice=1)
    mixer.play(wave_f7, voice=2)
    t_end = time.monotonic() + 3  # saves time 2 seconds in the future
    while time.monotonic() < t_end: # plays sparkels until time is up
        sparkles(.008)

# Main loop of game to keep track of time while updating states and inputs of the game
while True:

    currentTime = time.monotonic()

    if currentTime - previousTime > game_board_timer:
        #spkrenable.value = sound_switch.value
        previousTime = currentTime
        #print(game_over)
        #print(game_board_time_seconds)
        #print(total_yards)
        if not game_over: 
            game_board_time_seconds = game_board_time_seconds + 1
            mixer.play(wave_f1, voice=0, loop=True)
            #print("Game Time")
            #print(game_board_time_seconds)
            #print("Total Yards")
            #print(total_yards)
        
        if timer_toggle == True:
            timer_toggle = False
    
        else:
            timer_toggle = True
            
    # Check for timeout level_1
    if game_board_time_seconds > 10 and total_yards < level_2_yards:
        #print("Game Over...too slow for level 1")
        OutofTime()
        GameOver()
        
        # Check for timeout level_2
    if game_board_time_seconds > 20 and total_yards < level_3_yards:
        #print("Game Over...too slow for level 2")
        OutofTime()
        GameOver()
        
        # Check for timeout level_3
    if game_board_time_seconds > 30 and total_yards < level_4_yards:
        #print("Game Over...too slow for level 3")
        OutofTime()
        GameOver()
            # Check for timeout level_4    
    if game_board_time_seconds > 40 and total_yards < 100:
        #print("Game Over...too slow for level 4")
        OutofTime()
        GameOver()

    if lockout_left_move:
        
        if  button_left_move.value == True:
            
            #print(left_board_track[left_field_player_pixel])

            if total_yards == 0:
                game_over = False
                audio.play(mixer)
                
            total_yards = total_yards + 1
            
            if left_board_track[left_field_player_pixel] == 1:
                #print("Game Over Left!")
                pixels[left_field_player_pixel] = colors[0]
                pixels[right_field_player_pixel] = colors[6]
                audio.play(wave_f2)
                time.sleep(1)
                audio.play(wave_f4)
                for i in range(4):
                    pixels[left_field_player_pixel] = colors[0]
                    pixels[right_field_player_pixel] = colors[6]
                    time.sleep(.5)
                    pixels[left_field_player_pixel] = colors[6]
                    time.sleep(.5)
                GameOver()
            
            print(total_yards,game_board_time_seconds)
            
            if total_yards == win_game_yards:
                Flash()
                #print("Touchdown!") 
                GameOver()
                
            if total_yards%10==0 and not game_over:
                mixer.play(wave_f3, voice=1)
    
            if total_yards == level_2_yards:
                #print("Level 2!")
                Level2()
            
            if total_yards == level_3_yards:
                #print("Level 3!")
                Level3()
                
            if total_yards == level_4_yards:
                #print("Level 4!")
                Level4()
            
            for i in range(4):
                pixels[sel_pixels_left[i]] = colors[left_board_track[i]]
                pixels[9-sel_pixels_right[i]] = colors[right_board_track[i]]
                
            # Reassignment of tracking
            for i in range(4,0,-1):
                left_board_track[i] = left_board_track[i-1]
                right_board_track[i] = right_board_track[i-1]
            
            if not game_over:
                if random.random() > .5:
                    left_board_track[0] = 1
                    right_board_track[0] = 4
                else:
                    left_board_track[0] = 4
                    if random.random() > .5:
                        right_board_track[0] = 1
                    else:
                        right_board_track[0] = 4
                pixels[left_field_player_pixel] = colors[0]
                pixels[right_field_player_pixel] = colors[6]
            lockout_left_move= False
            
    else:
        
        if  button_left_move.value == False:
            lockout_left_move = True
            time.sleep(.1)	
		
    if lockout_right_move:
        if  button_right_move.value == True:
                    
            #print(right_board_track[9-right_field_player_pixel])
            
            if total_yards == 0:
                game_over = False 
                audio.play(mixer)
                
            total_yards = total_yards + 1
            
            if right_board_track[9-right_field_player_pixel] == 1:
                #print("Game Over Right!")
                pixels[right_field_player_pixel] = colors[0]
                pixels[left_field_player_pixel]=colors[6]
                audio.play(wave_f2)
                time.sleep(1)
                audio.play(wave_f4)
                for i in range(4):
                    pixels[right_field_player_pixel] = colors[0]
                    pixels[left_field_player_pixel]=colors[6]
                    time.sleep(.5)
                    pixels[right_field_player_pixel] = colors[6]
                    time.sleep(.5)
                GameOver()
            
            print(total_yards,game_board_time_seconds)
            
            if total_yards == win_game_yards:
                Flash()
                #print("Touchdown!")
                GameOver()
    
            if total_yards%10==0 and not game_over:
                mixer.play(wave_f3, voice=1)
                
            if total_yards == level_2_yards:
                #print("Level 2!")
                Level2()
            
            if total_yards == level_3_yards:
                #print("Level 3!")
                Level3()
                
            if total_yards == level_4_yards:
                #print("Level 4!")
                Level4()
            
            for i in range(4):
                pixels[sel_pixels_left[i]] = colors[left_board_track[i]]
                pixels[9-sel_pixels_right[i]] = colors[right_board_track[i]]
                
            # Reassignment of tracking
            for i in range(4,0,-1):
                left_board_track[i] = left_board_track[i-1]
                right_board_track[i] = right_board_track[i-1]
            
            if not game_over:
                if random.random() > .5:
                    left_board_track[0] = 1
                    right_board_track[0] = 4
                else:
                    left_board_track[0] = 4
                    if random.random() > .5:
                        right_board_track[0] = 1
                    else:
                        right_board_track[0] = 4
                        
                pixels[right_field_player_pixel] = colors[0]
                pixels[left_field_player_pixel] = colors[6]
        
            lockout_right_move = False
    else:
        if  button_right_move.value == False:
            lockout_right_move = True
            time.sleep(.1)	
		
            
            