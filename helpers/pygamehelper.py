import pygame
from pygame.locals import *
import os


        
class PygameHelper:
    def __init__(self):
		pass

    def get_spritesheet(self, im, coords):
        #array to store sprite images
        ss = []
    
        #create a path to the image passed in, and convert to pygame image
        mypath = os.path.dirname( os.path.realpath( __file__) )
        image = pygame.image.load( os.path.join(mypath, im) ).convert_alpha()
    
        #add each sprite to the sprite sheet array
        for set in coords:
            ss.append(image.subsurface(set))
        
        return ss
    #float range. Start=a, End=b, Step=c

    def frange(self, a, b, c):
        t = a
        while t < b:
            yield t
            t += c

    def drawGraph(self, screen, arr, step=5):
        maxy = screen.get_height()
        for i in range(len(arr)-1):
            x = i*step
            p1 = (i*step, maxy-arr[i])
            p2 = ((i+1)*step, maxy-arr[i+1])
            pygame.draw.line(screen, (0,0,0), p1, p2)
        
    
    #wait until a key is pressed, then return
    def waitForKey(self):
        press=False
        while not press:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    press = True
             
    #enter the main loop, possibly setting max FPS
            
    def update(self):
        pass
        
    def draw(self):
        pass
        
    def keyDown(self, key):
        pass
        
    def keyUp(self, key):
        pass
    
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        pass
        
