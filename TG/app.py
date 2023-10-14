from typing import Any
import pygame,sys

import TG.no_scene
import TG.TGnode

class APP:
    def __init__(self): #sceene是场景列表
        pygame.init()
        self.scene = []
        self.mode = 1
    def add(self,scene):
        self.scene.append(scene)
    def run_scene(self,scene): #设置启动场景
        self.run_scene = self.scene[scene]
    def run(self,size,mode,color):
        pygame.init()
        self.screen = pygame.display.set_mode(size,mode)
        while True:
            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    print("MrABCDEF")
                    pygame.quit()
                    sys.exit()
            if self.mode == 1:
                self.screen.fill(color)
                self.run_scene.update()
                self.run_scene.draw(self.screen)
                pygame.display.flip()
            elif self.mode == 0:
                self.run_scene = TG.no_scene.No()
    def pause(self):
        self.mode = 0

class Actor(pygame.sprite.Sprite,TG.TGnode.TGnode):
    def __init__(self,images,index):
        super().__init__([])
        self.index = index
        self.images = images
        self.image = images[self.index]
        self.rect = self.image.get_rect()
        self.position = self.rect.topleft
    def draw(self,surface):
        surface.blit(self.image,self.rect)
    def update(self):
        self.rect.topleft = self.position
        self.image = self.images[self.index]

class Text(Actor):
    def __init__(self, text, font, size, color):
        self.font = pygame.font.SysFont(font,size)
        self.image=self.font.render(text, True,color)
        self.images = [self.image]
        super().__init__(self.images,0)

class Scene(TG.TGnode.TGnode):
    def __init__(self):
        super().__init__()
        self.nodes = []
    def draw(self,screen):
        super().draw(screen)
    def update(self):
        super().update()
class Layer(TG.TGnode.TGnode):
    def __init__(self):
        self.more = pygame.sprite.Group()
        super().__init__()
        self.nodes = []
    def add(self, node):
        super().add(node)
        self.more.add(node)
    def update(self):
        self.more.update()
    def draw(self,screen):
        self.more.draw(screen)
