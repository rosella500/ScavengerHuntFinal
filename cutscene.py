from modes import ModeManager, GameMode, SimpleMode
import pygame

class Cutscene(GameMode):
    def __init__( self, image, sound, duration_in_milliseconds, next_mode_name ):
        '''
        Given a duration to show the splash screen 'duration_in_milliseconds',
        and the name of the next mode,
        displays 'image' until either a mouse click or 'duration_in_milliseconds'
        milliseconds have elapsed.
        '''
        ## Initialize the superclass.
        GameMode.__init__( self )
        
        self.image = image
        self.sound = sound
        self.duration = duration_in_milliseconds
        self.next_mode_name = next_mode_name
    
    def enter( self ):
        '''
        Reset the elapsed time and hide the mouse.
        '''
        self.so_far = 0
        pygame.mouse.set_visible( 0 )
        self.sound.play()
    
    def exit( self ):
        '''
        Show the mouse.
        '''
        pygame.mouse.set_visible( 1 )
        if (type(self.sound).__name__ != 'instance'):
            self.sound.stop()
    
    def draw( self, screen ):
        '''
        Draw the splash screen.
        '''
        screen.blit( self.image, ( 0,0 ) )
        pygame.display.flip()
    
    def update( self, clock ):
        '''
        Update the elapsed time.
        '''
        
        self.so_far += clock.get_time()
        
        ## Have we shown the image long enough?
        if self.so_far > self.duration:
            self.switch_to_mode( self.next_mode_name )
            
    def mouse_button_down(self,event):
        if (type(self.sound).__name__ != 'instance'):
            self.sound.stop()
        self.switch_to_mode(self.next_mode_name)
        
    def key_down(self,event):
        if event.key == K_ESCAPE:
            if (type(self.sound).__name__ != 'instance'):
                self.sound.stop()
            self.switch_to_mode(self.next_mode_name)