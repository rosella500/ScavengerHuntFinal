from modes import ModeManager, GameMode, SimpleMode
import pygame, os
from utils import *

class MainMenu( GameMode ):
    def __init__( self ):
        ## Initialize the superclass.
        GameMode.__init__( self )
        self.image, _ = load_image( 'MainMenu.jpg' )
        self.backgroundMusic = None
        ##load and play music
        try:
            self.backgroundMusic = os.path.join("data",'Eternal Memory.ogg')
            pygame.mixer.music.load( self.backgroundMusic )
            global splash_bool
            splash_bool = False
            global main_menu_bool
            main_menu_bool = True
        except pygame.error, message:
            print 'Cannot load music:'
            raise SystemExit, message
        self.start_rect = pygame.Rect( 13, 77, 159, 36 )
        self.quit_rect = pygame.Rect(14,117,97,32)
        
        self.mouse_down_pos = (-1,-1)
    
    def enter(self):
        pass
        pygame.mixer.music.load( self.backgroundMusic )
        pygame.mixer.music.play(1)
        
    def exit(self):
        pass
        pygame.mixer.music.stop()
    
    def mouse_button_down( self, event ):
        self.mouse_down_pos = event.pos
    
    def mouse_button_up( self, event ):
        
        def collides_down_and_up( r ):
            return r.collidepoint( self.mouse_down_pos ) and r.collidepoint( event.pos )
        
        if collides_down_and_up( self.start_rect ):
            print 'play!'
            global main_menu_bool
            main_menu_bool = False
            self.switch_to_mode( 'Intro' )
        if collides_down_and_up( self.quit_rect ):
            print 'Quit!'
            self.quit()
    
    def draw( self, screen ):
        ## Draw the HUD.
        screen.blit( self.image, ( 0,0 ) )
        pygame.display.flip()