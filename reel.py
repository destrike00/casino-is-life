from settings import *
import pygame,random

class Reel:
    def __init__(self,pos):
        self.symbol_list=pygame.sprite.Group()
        self.shuffled_keys=list(symbols.keys())
        print(self.shuffled_keys)
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys=self.shuffled_keys[:5] # in case there are more symbol options than the number of slots

        self.reel_is_spinning=False

        for idx,item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(symbols[item],pos,idx))
            pos=list(pos)
            pos[1]+=300
            pos=tuple(pos)

class Symbol(pygame.sprite.Sprite):
    def __init__(self,path,pos,idx):
        super().__init__()

        self.sym_type=path.split('/')[3].split('.')[0]

        self.pos=pos
        self.idx=idx
        self.image=pygame.image.load(path).convert_alpha()
        self.rect=self.image.get_rect(topleft=pos)
        self.x_val=self.rect.left

    def update(self):
        pass