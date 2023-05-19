import import_handler as shared
import Graph_and_Nodes
import game_sprites
import buttons


class SetupScreen:
    def __init__(self):
        self.font = shared.pygame.font.Font('ConsolaMono-Bold.ttf', 18)
        self.screen_done = False
        self.screen = shared.screen
        self.add_node_button_pressed = False
        self.clear_nodes_button_pressed = False
        self.game_start_button_pressed = False
        self.game_return_button_pressed = False
        self.dragging = False
        self.last_button = None
        self.manager = shared.TextInputManager(validator = lambda input: len(input) <= 15)
        self.selected_node = None
        self.previous_mouse_pos = None

        shared.pygame.time.set_timer(shared.pygame.USEREVENT, 600)
        self.next_screen = None
        self.screen_done = False
        self.buttons = buttons.Button()

        self.graph = Graph_and_Nodes.Graph() #Initiating an empty graph
        self.sprite_count = 0
        self.sprite_to_node = {} #Helping map a newly created sprite as a node in the graph
        self.sprite_group = shared.pygame.sprite.Group() #Initializing a sprite group
        self.connections = [] #This is just to help update the lines made between vertices
        self.start_vertex = None
        self.target_vertex = None
        # Set the double-click time threshold in milliseconds
        self.DOUBLE_CLICK_TIME = 250

        # Initialize the last_click_time and last_click_pos variables
        self.last_click_time = 0
        self.last_click_pos = None
        self.started = False
        self.shortest_path = None


        

    def get_mouse_pos(self):
        return shared.pygame.mouse.get_pos()

    def set_node_value(self):
        textinput_custom = shared.TextInputVisualizer(manager=self.manager, font_object=self.font)
        textinput_custom.cursor_width = 4
        textinput_custom.cursor_blink_interval = 500 # blinking interval in ms
        textinput_custom.cursor_color = shared.white
        textinput_custom.antialias = True
        textinput_custom.font_color = shared.white
        text_input_rect = shared.pygame.rect.Rect(240, 200, 250, 50)

        prompt = self.font.render('Type the value of this node and press enter: (You cannot repeat other node names!)', True, shared.white)
        prompt_rect = prompt.get_rect()
        prompt_rect.center = (690, 173)
        self.screen.blit(prompt, prompt_rect)  


        shared.pygame.key.set_repeat(200, 100)
        while True:
            #shared.screen.fill(shared.red)
            events = shared.pygame.event.get()
            for event in shared.pygame.event.get():
                if event.type == shared.pygame.QUIT:
                    shared.sys.exit()

            shared.pygame.draw.rect(self.screen, shared.black, text_input_rect)
            textinput_custom.update(events)
            shared.screen.blit(textinput_custom.surface, (240, 200))

            repeated_name = False
            for value in self.sprite_to_node.values():
                last_input = textinput_custom.value
                if value[0] == str(last_input):
                    repeated_name = True

            last_input = str(textinput_custom.value)

            if [ev for ev in events if ev.type == shared.pygame.KEYDOWN and ev.key == shared.pygame.K_RETURN] and repeated_name == False and len(last_input) > 0:
                textinput_custom.value = ''
                return last_input
        
            shared.pygame.display.flip()
            shared.clock.tick(60)


    def set_connection_value(self):
        textinput_custom = shared.TextInputVisualizer(manager=self.manager, font_object=self.font)
        textinput_custom.cursor_width = 4
        textinput_custom.cursor_blink_interval = 500 # blinking interval in ms
        textinput_custom.cursor_color = shared.white
        textinput_custom.antialias = True
        textinput_custom.font_color = shared.white
        text_input_rect = shared.pygame.rect.Rect(shared.screen_width/3, shared.screen_height/4.9, 250, 50)


        prompt = self.font.render('Type the weight of the connection between both nodes and press enter:', True, shared.white)
        prompt_rect = prompt.get_rect()
        prompt_rect.center = (shared.screen_width/2, shared.screen_height/5.5)
        self.screen.blit(prompt, prompt_rect)  


        shared.pygame.key.set_repeat(200, 100)
        while True:
            #shared.screen.fill(shared.red)
            events = shared.pygame.event.get()
            for event in shared.pygame.event.get():
                if event.type == shared.pygame.QUIT:
                    shared.sys.exit()

            shared.pygame.draw.rect(self.screen, shared.black, text_input_rect)
            textinput_custom.update(events)
            shared.screen.blit(textinput_custom.surface, (shared.screen_width/2, shared.screen_height/4.9))

            last_input = str(textinput_custom.value)

            if [ev for ev in events if ev.type == shared.pygame.KEYDOWN and ev.key == shared.pygame.K_RETURN] and len(last_input) > 0 and last_input.isdigit() and int(last_input) >= 1:
                textinput_custom.value = ''
                return int(last_input)
        
            shared.pygame.display.flip()
            shared.clock.tick(60)

    def print_start_vertex(self, value):
        font = shared.pygame.font.Font('ConsolaMono-Bold.ttf', 20)
        text = font.render("Start Vertex: " + value, True, shared.white)
        text_rect = text.get_rect()
        text_rect.center = (200, 125)
        self.screen.blit(text, text_rect)

    def print_target_vertex(self, value):
        font = shared.pygame.font.Font('ConsolaMono-Bold.ttf', 20)
        text = font.render("Target Vertex: " + value, True, shared.white)
        text_rect = text.get_rect()
        text_rect.center = (200, 165)
        self.screen.blit(text, text_rect)   

    def get_shortest_path(self):
        if self.shortest_path_dictionary != None and self.target_vertex != None:
            shortest_path_array = []
            curr_key = (self.target_vertex.value, self.shortest_path_dictionary[self.target_vertex.value][0])
            while curr_key[0] != self.start_vertex.value:

                shortest_path_array.append(curr_key)
                next_key = (self.shortest_path_dictionary[curr_key[0]][1][0], self.shortest_path_dictionary[curr_key[0]][0])
                if next_key != None:
                    curr_key = next_key
                else:
                    break
            shortest_path_array.append((self.start_vertex.value, 0))
            shortest_path_array.reverse()
            return shortest_path_array

    def display_shortest_path(self):
        font = shared.pygame.font.Font('ConsolaMono-Bold.ttf', 22)
        fastest_route_text = font.render('Fastest Route:', True, shared.white)
        fastest_route_text_rect = fastest_route_text.get_rect()
        fastest_route_text_rect.center = (shared.screen_width-200, shared.screen_height/4)
        self.screen.blit(fastest_route_text,fastest_route_text_rect)  

        height_counter = 50
        for vertex in self.shortest_path:
            path_text = font.render(vertex[0], True, shared.white)
            path_text_rect = path_text.get_rect()
            path_text_rect.center = (shared.screen_width-200, shared.screen_height/4+height_counter)

            path_value_text = font.render(str(vertex[1]), True, shared.white)
            path_value_text_rect = path_value_text.get_rect()
            path_value_text_rect.center = (shared.screen_width-95, shared.screen_height/4+height_counter)

            self.screen.blit(path_text, path_text_rect)
            self.screen.blit(path_value_text, path_value_text_rect)
            height_counter+=50

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

                # Check if this is a double click
                self.click_time = shared.pygame.time.get_ticks()
                self.click_pos = shared.pygame.mouse.get_pos()
                if self.last_click_pos == self.click_pos and self.click_time - self.last_click_time < self.DOUBLE_CLICK_TIME:
                    for i, sprite in enumerate(self.sprite_group):
                        if sprite.rect.collidepoint(event.pos) and self.started == False and self.start_vertex == None:
                            self.start_vertex = self.graph.nodes[i]
                            self.shortest_path_dictionary = self.graph.find_shortest_path(self.start_vertex)
                        elif sprite.rect.collidepoint(event.pos) and self.started == False and self.start_vertex != None:
                            self.target_vertex = self.graph.nodes[i] if self.graph.nodes[i] != self.start_vertex else None
                            if self.target_vertex != None:
                                print(self.start_vertex.value, self.target_vertex.value)
                self.last_click_time = self.click_time
                self.last_click_pos = self.click_pos

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
            elif event.button == 3:
                self.last_button = 3
                for i, sprite in enumerate(self.sprite_group):
                    if sprite.rect.collidepoint(event.pos):
                        self.selected_node = i
        elif event.type == shared.pygame.MOUSEBUTTONUP:
            if self.last_button == 1:
                if self.get_mouse_pos()[0] > self.buttons.add_node_button.left and self.get_mouse_pos()[0] < self.buttons.add_node_button.right and self.get_mouse_pos()[1] > self.buttons.add_node_button.top and self.get_mouse_pos()[1] < self.buttons.add_node_button.bottom:  
                    self.add_node_button_pressed = False
                    node_value = self.set_node_value()
                    new_vertex = game_sprites.Vertex(300, 300, node_value)
                    self.graph.add_node(node_value)
                    self.sprite_to_node[self.sprite_count] = [node_value, new_vertex]
                    self.sprite_group.add(new_vertex)
                    self.sprite_count+=1
                if self.get_mouse_pos()[0] > self.buttons.clear_node_button.left and self.get_mouse_pos()[0] < self.buttons.clear_node_button.right and self.get_mouse_pos()[1] > self.buttons.clear_node_button.top and self.get_mouse_pos()[1] < self.buttons.clear_node_button.bottom:
                    self.sprite_group = shared.pygame.sprite.Group()
                    self.graph = Graph_and_Nodes.Graph()
                    self.sprite_count = 0
                    self.sprite_to_node = {}
                    self.clear_nodes_button_pressed = False
                    self.connections = []
                    self.start_vertex = None
                    self.target_vertex = None
                    self.started = False
                    self.shortest_path_dictionary = None
                    self.shortest_path = None
                if self.get_mouse_pos()[0] > self.buttons.game_start_button.left and self.get_mouse_pos()[0] < self.buttons.game_start_button.right and self.get_mouse_pos()[1] > self.buttons.game_start_button.top and self.get_mouse_pos()[1] < self.buttons.game_start_button.bottom:
                    if self.start_vertex != None and self.target_vertex != None:
                        self.started = True
                        self.shortest_path = self.get_shortest_path()
                    self.game_start_button_pressed = False
                if self.get_mouse_pos()[0] > self.buttons.game_return_button.left and self.get_mouse_pos()[0] < self.buttons.game_return_button.right and self.get_mouse_pos()[1] > self.buttons.game_return_button.top and self.get_mouse_pos()[1] < self.buttons.game_return_button.bottom:
                    self.screen_done = True
                    self.next_screen = 'home_screen'
                    self.game_return_button_pressed = False
            elif self.last_button == 3 or self.last_button == None:
                if self.selected_node != None:
                    for j, sprite in enumerate(self.sprite_group):
                        if sprite.rect.collidepoint(self.get_mouse_pos()) and self.sprite_to_node[self.selected_node][0] != self.sprite_to_node[j][0]:
                            connection = (self.selected_node, j)
                            weight = self.set_connection_value()
                            self.graph.set_connections(self.graph.nodes[self.selected_node], self.graph.nodes[j], weight)
                            self.connections.append((connection, weight))

            self.last_button = None
            self.dragging = False
            self.dragged_sprite = None
            self.add_node_button_pressed = False
            self.clear_nodes_button_pressed = False
            self.game_start_button_pressed = False
            self.game_return_button_pressed = False
            self.selected_node = None
        elif event.type == shared.pygame.MOUSEMOTION:
            if self.last_button == 1:
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
        
        if self.started == True and self.shortest_path != None:
            self.display_shortest_path()

        self.sprite_group.draw(self.screen)
        for sprite in self.sprite_group:
            sprite.draw_value()

        if self.connections != []:
            for connection in self.connections:
                shared.pygame.draw.line(self.screen, shared.white, self.sprite_to_node[connection[0][0]][1].rect.center, self.sprite_to_node[connection[0][1]][1].rect.center, 5)
                weight = str(connection[1])
                font = shared.pygame.font.Font("ConsolaMono-Bold.ttf", 24)
                weight_text = font.render(weight, True, shared.white)
                weight_text_rect = weight_text.get_rect()
                weight_text_rect_x = (self.sprite_to_node[connection[0][0]][1].rect.center[0]+self.sprite_to_node[connection[0][1]][1].rect.center[0])/2
                weight_text_rect_y = (self.sprite_to_node[connection[0][0]][1].rect.center[1]+self.sprite_to_node[connection[0][1]][1].rect.center[1])/2 - 25
                weight_text_rect.center =(weight_text_rect_x, weight_text_rect_y)
                self.screen.blit(weight_text, weight_text_rect)

        if self.start_vertex != None:
            self.print_start_vertex(self.start_vertex.value)
        if self.target_vertex != None:
            self.print_target_vertex(self.target_vertex.value)  

    def is_done(self):
        if self.screen_done == True:
            return True
        else:
            return False

