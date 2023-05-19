import import_handler as shared
import Graph_and_Nodes
import game_sprites
import buttons

class SetupScreen:
    def __init__(self):
        self.screen_done = False
        self.screen = shared.screen
        self.add_node_button_pressed = False
        self.clear_nodes_button_pressed = False
        self.game_start_button_pressed = False
        self.game_return_button_pressed = False
        self.dragging = False
        self.last_button = None

        shared.pygame.time.set_timer(shared.pygame.USEREVENT, 600)
        self.next_screen = None
        self.screen_done = False
        self.buttons = buttons.Button()

        self.graph = Graph_and_Nodes.Graph() #Initiating an empty graph
        self.sprite_to_node = {} #Helping map a newly created sprite as a node in the graph
        self.sprite_group = shared.pygame.sprite.Group() #Initializing a sprite group

    def get_mouse_pos(self):
        return shared.pygame.mouse.get_pos()

    def handle_event(self, event):
        # Handle any user input, such as button clicks
        if event.type == shared.pygame.QUIT:
            shared.sys.exit()
        if event.type == shared.pygame.USEREVENT: #Making each ball created go up and down
            for sprite in self.sprite_group:
                sprite.update()
                sprite.dx*=-1
        if event.type == shared.pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.last_button = 1
                if self.get_mouse_pos()[0] > self.buttons.add_node_button.left and self.get_mouse_pos()[0] < self.buttons.add_node_button.right and self.get_mouse_pos()[1] > self.buttons.add_node_button.top and self.get_mouse_pos()[1] < self.buttons.add_node_button.bottom:
                    self.add_node_button_pressed = True
                if self.get_mouse_pos()[0] > self.buttons.clear_node_button.left and self.get_mouse_pos()[0] < self.buttons.clear_node_button.right and self.get_mouse_pos()[1] > self.buttons.clear_node_button.top and self.get_mouse_pos()[1] < self.buttons.clear_node_button.bottom:
                    self.clear_nodes_button_pressed = True
                if self.get_mouse_pos()[0] > self.buttons.game_start_button.left and self.get_mouse_pos()[0] < self.buttons.game_start_button.right and self.get_mouse_pos()[1] > self.buttons.game_start_button.top and self.get_mouse_pos()[1] < self.buttons.game_start_button.bottom:
                    self.game_start_button_pressed = True
                if self.get_mouse_pos()[0] > self.buttons.game_return_button.left and self.get_mouse_pos()[0] < self.buttons.game_return_button.right and self.get_mouse_pos()[1] > self.buttons.game_return_button.top and self.get_mouse_pos()[1] < self.buttons.game_return_button.bottom:
                    self.game_return_button_pressed = True
                for sprite in self.sprite_group:
                    if sprite.rect.collidepoint(event.pos):
                        self.dragging = True
                        self.dragged_sprite = sprite
        elif event.type == shared.pygame.MOUSEBUTTONUP:
            if self.last_button == 1:
                if self.get_mouse_pos()[0] > self.buttons.add_node_button.left and self.get_mouse_pos()[0] < self.buttons.add_node_button.right and self.get_mouse_pos()[1] > self.buttons.add_node_button.top and self.get_mouse_pos()[1] < self.buttons.add_node_button.bottom:
                    self.add_node_button_pressed = False
                    new_vertex = game_sprites.Vertex(300, 300)
                    self.sprite_group.add(new_vertex)
                if self.get_mouse_pos()[0] > self.buttons.clear_node_button.left and self.get_mouse_pos()[0] < self.buttons.clear_node_button.right and self.get_mouse_pos()[1] > self.buttons.clear_node_button.top and self.get_mouse_pos()[1] < self.buttons.clear_node_button.bottom:
                    self.sprite_group = shared.pygame.sprite.Group()
                    self.clear_nodes_button_pressed = False
                if self.get_mouse_pos()[0] > self.buttons.game_start_button.left and self.get_mouse_pos()[0] < self.buttons.game_start_button.right and self.get_mouse_pos()[1] > self.buttons.game_start_button.top and self.get_mouse_pos()[1] < self.buttons.game_start_button.bottom:
                    self.game_start_button_pressed = False
                if self.get_mouse_pos()[0] > self.buttons.game_return_button.left and self.get_mouse_pos()[0] < self.buttons.game_return_button.right and self.get_mouse_pos()[1] > self.buttons.game_return_button.top and self.get_mouse_pos()[1] < self.buttons.game_return_button.bottom:
                    self.screen_done = True
                    self.next_screen = 'home_screen'
                    self.game_return_button_pressed = False

            self.last_button = None
            self.dragging = False
            self.dragged_sprite = None
            self.add_node_button_pressed = False
            self.clear_nodes_button_pressed = False
            self.game_start_button_pressed = False
            self.game_return_button_pressed = False

        elif event.type == shared.pygame.MOUSEMOTION:
            if self.dragging and self.dragged_sprite is not None:
                self.dragged_sprite.rect.move_ip(event.rel)


    def update(self):
        pass

    def draw(self):
        self.screen.fill(shared.black)
        if self.add_node_button_pressed == False:
            self.buttons.create_add_node_button()
        elif self.add_node_button_pressed == True:
            self.buttons.shrink_add_node_button()

        if self.clear_nodes_button_pressed == False:
            self.buttons.create_clear_nodes_button()
        elif self.clear_nodes_button_pressed == True:
            self.buttons.shrink_clear_nodes_button()

        if self.game_start_button_pressed == False:
            self.buttons.create_game_start_button()
        elif self.game_start_button_pressed == True:
            self.buttons.shrink_game_start_button()
        
        if self.game_return_button_pressed == False:
            self.buttons.create_game_return_button()
        elif self.game_return_button_pressed == True:
            self.buttons.shrink_game_return_button()

        self.sprite_group.draw(self.screen)

    def is_done(self):
        if self.screen_done == True:
            return True
        else:
            return False

