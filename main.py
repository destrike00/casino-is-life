from settings import *
from machine import Machine
import pygame,sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Ginoka kaszinoja')
        self.clock=pygame.time.Clock()
        self.bg_image=pygame.image.load(BG_IMAGE_PATH)

        #create slotmachine class
        self.machine=Machine()
        self.delta_time=0

        #main_sound=pygame.mixer.Sound("audio/track.mp3")
        #main_sound.play(loops=-1)

    def run(self):
        self.start_time = pygame.time.get_ticks()
        while True:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.delta_time=(pygame.time.get_ticks()-self.start_time)/1000
            self.start_time=pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blit(self.bg_image,(0,0))
            self.machine.update(self.delta_time)
            self.clock.tick(FPS)



if __name__=='__main__':

    game=Game()
    game.run()

