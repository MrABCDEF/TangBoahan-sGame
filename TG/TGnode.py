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