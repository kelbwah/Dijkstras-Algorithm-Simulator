import import_handler as shared
import buttons

class InfoScreen:
    def __init__(self):
        self.screen_done = False
        self.font = shared.pygame.font.Font('ConsolaMono-Bold.ttf', 24)
        self.screen = shared.screen
        self.return_button_clicked = False
        self.next_screen = None
        self.buttons = buttons.Button()

    def get_mouse_pos(self):
        return shared.pygame.mouse.get_pos()

    def handle_event(self, event):
        # Handle any user input, such as button clicks
        if event.type == shared.pygame.QUIT:
            shared.sys.exit()
        if event.type == shared.pygame.MOUSEBUTTONDOWN:
            #Pressed start button
            if self.get_mouse_pos()[0] > self.buttons.return_button.left and self.get_mouse_pos()[0] < self.buttons.return_button.right and self.get_mouse_pos()[1] > self.buttons.return_button.top and self.get_mouse_pos()[1] < self.buttons.return_button.bottom:
                self.return_button_clicked = True
        elif event.type == shared.pygame.MOUSEBUTTONUP:
            #Pressed start button
            if self.get_mouse_pos()[0] > self.buttons.return_button.left and self.get_mouse_pos()[0] < self.buttons.return_button.right and self.get_mouse_pos()[1] > self.buttons.return_button.top and self.get_mouse_pos()[1] < self.buttons.return_button.bottom:
                self.return_button_clicked = False
                self.screen_done = True
                self.next_screen = 'home_screen'
            self.return_button_clicked = False

    def create_info_text(self):
        self.info_text_1 = self.font.render('Welcome to Dijkstra\'s algorithm simulation where you will learn visually how this', True, shared.white)
        self.info_text_rect_1 = self.info_text_1.get_rect()
        self.info_text_rect_1.center = (shared.screen_width/2, shared.screen_height/4)

        self.info_text_2 = self.font.render('algorithm works through this interactive simulation. You will be able to drag', True, shared.white)
        self.info_text_rect_2 = self.info_text_2.get_rect()
        self.info_text_rect_2.center = (shared.screen_width/2, shared.screen_height/3.2)

        self.info_text_3 = self.font.render('and drop nodes to the screen and connect them with a specific weight, then you are able', True, shared.white)
        self.info_text_rect_3 = self.info_text_3.get_rect()
        self.info_text_rect_3.center = (shared.screen_width/2, shared.screen_height/2.65)

        self.info_text_4 = self.font.render('to choose any start node and end node and look at the fastest route between both nodes!', True, shared.white)
        self.info_text_rect_4 = self.info_text_4.get_rect()
        self.info_text_rect_4.center = (shared.screen_width/2, shared.screen_height/2.25)

        self.screen.blit(self.info_text_1, self.info_text_rect_1)
        self.screen.blit(self.info_text_2, self.info_text_rect_2)
        self.screen.blit(self.info_text_3, self.info_text_rect_3)
        self.screen.blit(self.info_text_4, self.info_text_rect_4)

    def update(self):
        pass

    def draw(self):
        self.screen.fill(shared.black)
        self.create_info_text()
        if self.return_button_clicked == False:
            self.buttons.create_return_button()
        elif self.return_button_clicked == True:
            self.buttons.shrink_return_button()

    def is_done(self):
        if self.screen_done == True:
            return True
        else:
            return False