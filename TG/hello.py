import TG.app
import pygame

a = TG.app.APP()

scene = TG.app.Scene()

layer = TG.app.Layer()

Text = TG.app.Text("HelloWorld",None,64,(125,125,125))

scene.add(layer)

layer.add(Text)

a.add(scene)

a.run_scene(0)

a.run((320,180),pygame.RESIZABLE,(255,255,255))