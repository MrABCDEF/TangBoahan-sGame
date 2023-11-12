import TG.app
import pygame

a = TG.app.APP() #程序控制体，APP，APP也可以继承TGnode，主要可以每帧执行子节点（运行节点）的update函数，并且执行draw函数。

scene = TG.app.Scene()#一个关系，可以只有一个图层，角色绘制随机。

layer = TG.app.Layer()

class T(TG.app.Text):
    def __init__(self, text, font, size, color):
        super().__init__(text, font, size, color)
    def update(self):
        super().update()
        aaa = self.event
        self.position = aaa[1][1]
Text = T("HelloWorld",None,100,(0,0,0))

scene.add(layer)

layer.add(Text)

a.add(scene)

a.run_scene(0)

a.run((320,180),pygame.RESIZABLE,(255,255,255))