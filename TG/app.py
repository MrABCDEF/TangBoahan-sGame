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
        self.rect = self.screen.get_rect()
        self.run_scene.get_screen(self.screen)
        while True:
            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    print("MrABCDEF at GitHub!")
                    pygame.quit()
                    sys.exit()
            pygame.event.get()
            self.key = pygame.key.get_pressed()
            self.mouse = [pygame.mouse.get_pressed(),pygame.mouse.get_pos()]
            if self.mode == 1:
                self.screen.fill(color)
                self.run_scene.get_event([self.key,self.mouse])
                self.run_scene.update()
                self.run_scene.draw(self.screen)
                pygame.display.flip()
                
            elif self.mode == 0:
                pass
    def pause(self):
        self.mode = 0
    def running(self):
        self.mode = 1
    def quit(self):
        pygame.quit()
        sys.exit()


class Actor(TG.TGnode.TGnode):
    def __init__(self, images, index):
        super().__init__()
        self.index = index
        self.images = images
        self.image = images[self.index]
        self.rect = self.image.get_rect()
        self.position = [0,0] 
    def draw(self,surface):
        surface.blit(self.image,self.rect)
    def update(self):
        self.rect.topleft = self.position
        self.image = self.images[self.index]
    def move(self,x,y):
        self.position[0]+=x
        self.position[1]+=y
    def move_x(self,num):
        self.position[0]+=num
    def move_y(self,num):
        self.position[1]+=num
    def rotozoon(self,num1,num2):
        pygame.transform.rotozoom(self.image,num1,num2)

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
        super().__init__()
        self.nodes = []
    def add(self, node):
        super().add(node)
    def update(self):
        super().update()
    def draw(self,screen):
        super().draw(screen)
    

class MomActor(TG.TGnode.TGnode):
    def __init__(self):
        super().__init__()
        self.son = pygame.sprite.Group()
    def add(self,son):
        self.son.add(son)
    def update(self):
        super().update()
        self.son.update()
    def draw(self, screen):
        super().draw
        self.son.draw(screen)