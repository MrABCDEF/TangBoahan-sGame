class TGnode:
    def __init__(self):
        self.nodes = []
    def add(self, node):
        self.nodes.append(node)
    def update(self):
        update = 0
        for xupdate in self.nodes:
            self.nodes[update].update()
    def draw(self,screen):
        draw = 0
        for xdraw in self.nodes:
            self.nodes[draw].draw(screen)
    def get_screen(self,screen):
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
    def get_event(self,event):
        a = 0
        for x in self.nodes:
            self.nodes[a].get_event(event)
            a = a+1
        self.event = event 