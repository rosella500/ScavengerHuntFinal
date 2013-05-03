#!/opt/local/bin/python2.7

import os, pygame, json, csv
from cutscene import *
from hotspot import *
from exit_class import *
from room import *
from pause_menu import *
from movieScene import *
from pygame.locals import *
from utils import *
from mainMenu import *
from modes import ModeManager, GameMode, SimpleMode

kDataDir = 'data'
kGlobals = 'globals.json'
globals = ''

#used to prevent from pausing during splashscreen or main menu
global splash_bool
splash_bool = True
global main_menu_bool
main_menu_bool = False

##Keep track of last gameMode (room)
global lastMode
  
        
def main():
    ### Load global variables.
    globals = json.load( open( os.path.join( kDataDir, kGlobals ) ) )
    
    
    ### Initialize pygame.
    pygame.init()
    screen = pygame.display.set_mode( globals['screen_size'] )
    pygame.display.set_caption( globals['window_title'] )
    clock = pygame.time.Clock()
    
    
    ### Set up the modes.
    modes = ModeManager()
    
    
    ### Set up Splash Screen
    image, _ = load_image( 'Splash.jpg' )
    modes.register_mode('SplashScreen',Cutscene(image,load_sound('None'),3000,'MainMenu'))
    
    ### Set up Main Menu
    modes.register_mode('MainMenu', MainMenu())
    
    
    ## Set up intro cutscene modes.
    image, _ = load_image( 'BlackScreen.png' )
    sound = load_sound('MichelleIntro.wav')
    modes.register_mode( 'Intro', Cutscene(image, sound, 21000, 'Sleep' ) )
    
    image, _ = load_image( 'WakeUp.jpg' )
    sound = load_sound('AhGloriousSleep.wav')
    modes.register_mode( 'Sleep', Cutscene(image, sound, 8000, 'Huh' ) )
    
    image, _ = load_image( 'NotePillowSansArrow.jpg' )
    sound = load_sound('HuhWhatsThisAndOpen.wav')
    modes.register_mode( 'Huh', Cutscene(image, sound, 5000, 'Note' ) )
    
    image, _ = load_image( 'Note.jpg' )
    sound = load_sound('CarolineNote.wav')
    modes.register_mode( 'Note', Cutscene(image, sound, 22000, 'Room' ) )

    ##Set up bathroom cutscene
    modes.register_mode( 'Flashback', MovieScene('flashback.mpg','DoorsCutscene' ) )
    
    image, _ = load_image( 'Doors.jpg' )
    sound = load_sound('AfterHallucination.wav')
    modes.register_mode( 'DoorsCutscene', Cutscene(image, sound, 13000, 'StairsCutscene' ) )
    
    image, _ = load_image( 'Stairs.jpg' )
    sound = load_sound('Stairs.wav')##Footsteps
    modes.register_mode( 'StairsCutscene', Cutscene(image, sound, 2000, 'BathroomCutscene' ) )
    
    image, _ = load_image( 'Bathroom.jpg' )
    sound = load_sound('None')
    modes.register_mode( 'BathroomCutscene', Cutscene(image, sound, 1000, 'SinkCutscene' ) )

    image, _ = load_image( 'Sink.jpg' )
    sound = load_sound('Sink.wav')
    modes.register_mode( 'SinkCutscene', Cutscene(image, sound, 2000, 'TrackmarksCutscene' ) )

    image, _ = load_image( 'TrackMarks.jpg' )
    sound = load_sound('TrackMarks.wav')
    modes.register_mode( 'TrackmarksCutscene', Cutscene(image, sound, 14000, 'StairsCutscene2' ) )

    image, _ = load_image( 'Stairs.jpg' )
    sound = load_sound('Stairs.wav')##Footsteps
    modes.register_mode( 'StairsCutscene2', Cutscene(image, sound, 2000, 'BedroomNote' ) )

    image, _ = load_image( 'BedWithCombination.jpg' )
    sound = load_sound('WhereCombination.wav')
    modes.register_mode( 'BedroomNote', Cutscene(image, sound, 4000, 'CombinationCutscene' ) )

    image, _ = load_image( 'Combination.jpg' )
    sound = load_sound('Combination.wav')
    modes.register_mode( 'CombinationCutscene', Cutscene(image, sound, 3000, 'Room' ) )

    ##Set up ending cutscene
    image, _ = load_image( 'InsideBox.jpg' )
    modes.register_mode('End', Cutscene(image, load_sound('None'), 5000, 'EndLetter'))

    image, _ = load_image( 'AtticLetter.jpg' )
    sound = load_sound('PaperOpening.wav')
    modes.register_mode('EndLetter', Cutscene(image, sound, 2000, 'EndLetterOpen'))

    image, _ = load_image( 'AtticLetterOpen.jpg' )
    sound = load_sound('EndAtticNote.wav')
    modes.register_mode('EndLetterOpen', Cutscene(image, sound, 14000, 'EndBoxBottom'))

    image, _ = load_image( 'InsideBoxWithoutLetter.jpg' )
    sound = load_sound('PaperOpening.wav')
    modes.register_mode('EndBoxBottom', Cutscene(image, sound, 2000, 'EndFinal'))

    image, _ = load_image( 'FinalMirror.jpg' )
    sound = load_sound('End.wav')
    modes.register_mode('EndFinal', Cutscene(image, sound, 10000, 'MainMenu'))
    
    pause_menu = PauseMenu()
    modes.register_mode('PauseMenu', pause_menu)


    room = Room()
    modes.register_mode('Room', room)
    
    ## Start with Splash
    modes.switch_to_mode( 'SplashScreen' )

    pause = False
    
    ### The main loop.
    fps = globals['fps']
    while not modes.quitting():
        clock.tick( fps )
        
        ## Handle Input Events
        for event in pygame.event.get():
            
            if event.type == QUIT:
                modes.switch_to_mode(None)
                break
            
            elif event.type == KEYDOWN:
                key = pygame.key.get_pressed()
                #print(key)#test
                global splash_bool
                global main_menu_bool
                if (key[K_ESCAPE] or key[K_p]) and (splash_bool == False and main_menu_bool == False):
                    if pause == True:
                        modes.switch_to_mode( 'Room' )
                        pause = False
                        print("game unpaused")
                    elif pause == False:
                        #need some function to update the current note
                        #pause_menu.someMethod()
                        pause_menu.update_current_note(room.globals['current_note'])
                        modes.switch_to_mode( 'PauseMenu' )
                        pause = True
                        print("game paused")
                    else:
                        print("ERROR:  pause variable is not FALSE nor TRUE")
                else:
                    print("some key pressed")
                modes.current_mode.key_down( event )
            
            elif event.type == KEYUP:
                modes.current_mode.key_up( event )
            
            elif event.type == MOUSEMOTION:
                modes.current_mode.mouse_motion( event )
            
            elif event.type == MOUSEBUTTONUP:
                modes.current_mode.mouse_button_up( event )
            
            elif event.type == MOUSEBUTTONDOWN:
                modes.current_mode.mouse_button_down( event )
        
        modes.current_mode.update( clock )
        modes.current_mode.draw( screen )
    
    
    ### Game over.
    


## this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
