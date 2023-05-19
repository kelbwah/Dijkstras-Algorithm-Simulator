import import_handler as shared
import buttons

class HomeScreen:
    def __init__(self):
        #Initializing title text
        self.font = shared.pygame.font.Font('ConsolaMono-Bold.ttf', 36)
        self.screen = shared.screen
        self.welcome_text = self.font.render("Dijkstra\'s Algorithm Simulator", True, shared.white)
        self.welcome_text_rect = self.welcome_text.get_rect(center = (shared.screen_width/2, shared.screen_height/10))
        self.next_screen = None
        self.buttons = buttons.Button()
        
        #Initializing counters used to be able to make the title text go up and down
        self.counter = 0
        self.other_counter = 1

        #Initializing variables to see whether or not certain buttons are pressed and if they are, depending on which button is pressed, it will go to a new page 
        self.screen_done = False
        self.start_button_clicked = False
        self.info_button_clicked = False
        self.exit_button_clicked = False
  
    def get_mouse_pos(self):
        return shared.pygame.mouse.get_pos()

    def handle_event(self, event):
        # Handle any user input, such as button clicks
        if event.type == shared.pygame.QUIT:
            shared.sys.exit()
        if event.type == shared.pygame.MOUSEBUTTONDOWN:
            #Pressed start button
            if self.get_mouse_pos()[0] > self.buttons.start_button.left and self.get_mouse_pos()[0] < self.buttons.start_button.right and self.get_mouse_pos()[1] > self.buttons.start_button.top and self.get_mouse_pos()[1] < self.buttons.start_button.bottom:
                self.start_button_clicked = True
            elif self.get_mouse_pos()[0] > self.buttons.info_button.left and self.get_mouse_pos()[0] < self.buttons.info_button.right and self.get_mouse_pos()[1] > self.buttons.info_button.top and self.get_mouse_pos()[1] < self.buttons.info_button.bottom:
                self.info_button_clicked = True
            elif self.get_mouse_pos()[0] > self.buttons.exit_button.left and self.get_mouse_pos()[0] < self.buttons.exit_button.right and self.get_mouse_pos()[1] > self.buttons.exit_button.top and self.get_mouse_pos()[1] < self.buttons.exit_button.bottom:
                self.exit_button_clicked = True
        elif event.type == shared.pygame.MOUSEBUTTONUP:
            if self.get_mouse_pos()[0] > self.buttons.start_button.left and self.get_mouse_pos()[0] < self.buttons.start_button.right and self.get_mouse_pos()[1] > self.buttons.start_button.top and self.get_mouse_pos()[1] < self.buttons.start_button.bottom:
                self.next_screen = "setup_screen"
                self.start_button_clicked = False
                self.screen_done = True
            elif self.get_mouse_pos()[0] > self.buttons.info_button.left and self.get_mouse_pos()[0] < self.buttons.info_button.right and self.get_mouse_pos()[1] > self.buttons.info_button.top and self.get_mouse_pos()[1] < self.buttons.info_button.bottom:
                self.next_screen = "info_screen"
                self.info_button_clicked = False
                self.screen_done = True
            elif self.get_mouse_pos()[0] > self.buttons.exit_button.left and self.get_mouse_pos()[0] < self.buttons.exit_button.right and self.get_mouse_pos()[1] > self.buttons.exit_button.top and self.get_mouse_pos()[1] < self.buttons.exit_button.bottom:
                self.exit_button_clicked = False
                self.screen_done = True
                shared.sys.exit()
            self.start_button_clicked = False
            self.info_button_cliced = False
            self.exit_button_clicked = False

    def welcome_text_up(self):
        self.welcome_text_rect.y-=20
        self.welcome_text_rect.x+=20
    
    def welcome_text_down(self):
        self.welcome_text_rect.y+=10
        self.welcome_text_rect.x-=10

    def update(self):
        self.counter+=1

        #Moving the title text down
        if self.counter % 50 == 0:
            self.welcome_text_down()
            self.other_counter+=1

        #Moving the title text up
        if self.other_counter % 3 == 0:
            self.welcome_text_up()
            self.other_counter+=1

    def draw(self):
        #Creating black screen
        self.screen.fill(shared.black)
        
        #Creating welcome_text in the middle of screen
        self.screen.blit(self.welcome_text, self.welcome_text_rect)

        #Creating start button
        if self.start_button_clicked == False:
            self.buttons.create_start_button()
        elif self.start_button_clicked == True:
            self.buttons.shrink_start_button()

        #Creating info button
        if self.info_button_clicked == False:
            self.buttons.create_info_button()
        elif self.info_button_clicked == True:
            self.buttons.shrink_info_button()

        #Creating exit button
        if self.exit_button_clicked == False:
            self.buttons.create_exit_button()
        elif self.exit_button_clicked == True:
            self.buttons.shrink_exit_button()
            
    def is_done(self):
        # Return True if the screen is finished and we should move to the next screen
        if self.screen_done == True:
            return True
        else:
            return False
        

