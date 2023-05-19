import import_handler as shared
import Graph_and_Nodes

class Vertex(shared.pygame.sprite.Sprite):
    def __init__(self, x, y, value):
        shared.pygame.sprite.Sprite.__init__(self)
        self.font = shared.pygame.font.Font('ConsolaMono-Bold.ttf', 24)
        self.x = x
        self.y = y
        self.dx = 10
        self.screen = shared.screen
        self.image = shared.pygame.image.load('ball_sprite.png').convert_alpha()
        self.image = shared.pygame.transform.scale(self.image, (98, 196))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.value = value

    def update(self):
        self.rect.move_ip(0, self.dx)

    def set_value(self, value):
        self.value = value
    
    def draw_value(self):
        prompt = self.font.render(self.value, True, shared.white)
        prompt_rect = prompt.get_rect()
        prompt_rect.center = (self.rect.center[0], self.rect.center[1])
        self.screen.blit(prompt, prompt_rect)  


class Player(shared.pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        shared.pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.x = x
        self.y = y
        self.screen = shared.screen
        self.square = shared.pygame.Rect(self.x, self.y, 100, 100)

    def update(self):
        pass
    
    def draw(self):
        shared.pygame.draw.rect(self.screen, self.color, self.square)        