from modes import ModeManager, GameMode, SimpleMode
import pygame, os
from utils import *

class MovieScene(GameMode):
    def __init__( self, movie, next_mode_name ):
        '''
        Given the file name of a movie, will play that movie until it is over
        and then transition to the next mode
        '''
        ## Initialize the superclass.
        GameMode.__init__( self )
        
        self.movieName = movie
        self.next_mode_name = next_mode_name
        self.movie = None
        
    
    def enter( self ):
        '''
        Reset the elapsed time and hide the mouse.
        '''
        
        pygame.mixer.music.load(os.path.join( 'data',self.movieName))
        self.movie = pygame.movie.Movie(os.path.join( 'data',self.movieName))
        if self.movie.has_video():
            pygame.mixer.music.play()
            self.movie.play()
            
        self.duration = self.movie.get_length() * 1000
        
        self.so_far = 0
        pygame.mouse.set_visible( 0 )
    
    def exit( self ):
        '''
        Show the mouse.
        '''
        pygame.mouse.set_visible( 1 )
        pygame.mixer.init()
        self.movie.stop()
    
    def update( self, clock ):
        '''
        Update the elapsed time.
        '''
        
        self.so_far += clock.get_time()
        
        ## Have we shown the image long enough?
        if self.so_far > self.duration:
            #enableMixer()
            self.switch_to_mode( self.next_mode_name )
