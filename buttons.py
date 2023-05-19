import import_handler as shared

class Button:
    def __init__(self):
        self.game_and_home_screen_button_font = shared.pygame.font.Font('ConsolaMono-Bold.ttf', 22)
        self.info_screen_button_font = shared.pygame.font.Font('ConsolaMono-Bold.ttf', 24)
        self.screen = shared.screen
    
    def shrink_start_button(self):
        self.start_button_shade = shared.pygame.Rect(shared.screen_width/2 - (225/2), shared.screen_height / 4, 235, 75)
        self.start_button = shared.pygame.Rect(shared.screen_width/2 - (225/2), shared.screen_height / 4, 225, 65)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.start_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.start_button)
        self.start_button_text = self.game_and_home_screen_button_font.render('Start', True, (0,0,0))
        self.start_button_text_rect = self.start_button_text.get_rect()
        self.start_button_text_rect.center=self.start_button.center
        self.screen.blit(self.start_button_text, self.start_button_text_rect)

    def create_start_button(self):
        #Start buttons
        self.start_button_shade = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 4, 245, 85)
        self.start_button = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 4, 235, 75)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.start_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.start_button)
        self.start_button_text = self.game_and_home_screen_button_font.render('Start', True, (0,0,0))
        self.start_button_text_rect = self.start_button_text.get_rect()
        self.start_button_text_rect.center=self.start_button.center
        self.screen.blit(self.start_button_text, self.start_button_text_rect)

    def shrink_info_button(self):
        #Start buttons
        self.info_button_shade = shared.pygame.Rect(shared.screen_width/2 - (225/2), shared.screen_height / 2, 235, 75)
        self.info_button = shared.pygame.Rect(shared.screen_width/2 - (225/2), shared.screen_height / 2, 225, 65)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.info_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.info_button)
        self.info_button_text = self.game_and_home_screen_button_font.render('Info', True, (0,0,0))
        self.info_button_text_rect = self.info_button_text.get_rect()
        self.info_button_text_rect.center=self.info_button.center
        self.screen.blit(self.info_button_text, self.info_button_text_rect)

    def create_info_button(self):
        #Start buttons
        self.info_button_shade = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 2, 245, 85)
        self.info_button = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 2, 235, 75)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.info_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.info_button)
        self.info_button_text = self.game_and_home_screen_button_font.render('Info', True, (0,0,0))
        self.info_button_text_rect = self.info_button_text.get_rect()
        self.info_button_text_rect.center=self.info_button.center
        self.screen.blit(self.info_button_text, self.info_button_text_rect)

    def shrink_exit_button(self):
        #Start buttons
        self.exit_button_shade = shared.pygame.Rect(shared.screen_width/2 - (225/2), shared.screen_height / 1.3, 235, 75)
        self.exit_button = shared.pygame.Rect(shared.screen_width/2 - (225/2), shared.screen_height / 1.3, 225, 65)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.exit_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.exit_button)
        self.exit_button_text = self.game_and_home_screen_button_font.render('Exit', True, (0,0,0))
        self.exit_button_text_rect = self.exit_button_text.get_rect()
        self.exit_button_text_rect.center=self.exit_button.center
        self.screen.blit(self.exit_button_text, self.exit_button_text_rect)

    def create_exit_button(self):
        #Start buttons
        self.exit_button_shade = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 1.3, 245, 85)
        self.exit_button = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 1.3, 235, 75)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.exit_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.exit_button)
        self.exit_button_text = self.game_and_home_screen_button_font.render('Exit', True, (0,0,0))
        self.exit_button_text_rect = self.exit_button_text.get_rect()
        self.exit_button_text_rect.center=self.exit_button.center
        self.screen.blit(self.exit_button_text, self.exit_button_text_rect)

    def shrink_return_button(self):
        self.return_button_shade = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 1.5, 235, 75)
        self.return_button = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 1.5, 225, 65)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.return_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.return_button)
        self.return_button_text = self.info_screen_button_font.render('Back', True, (0,0,0))
        self.return_button_text_rect = self.return_button_text.get_rect()
        self.return_button_text_rect.center = self.return_button.center
        self.screen.blit(self.return_button_text, self.return_button_text_rect)

    def create_return_button(self):
        self.return_button_shade = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 1.5, 245, 85)
        self.return_button = shared.pygame.Rect(shared.screen_width/2 - (235/2), shared.screen_height / 1.5, 235, 75)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.return_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.return_button)
        self.return_button_text = self.info_screen_button_font.render('Back', True, (0,0,0))
        self.return_button_text_rect = self.return_button_text.get_rect()
        self.return_button_text_rect.center = self.return_button.center
        self.screen.blit(self.return_button_text, self.return_button_text_rect)  

    def shrink_clear_nodes_button(self):
        self.clear_node_button_shade = shared.pygame.Rect(shared.screen_width/2.67 - (215/2), shared.screen_height / 16, 215, 55)
        self.clear_node_button = shared.pygame.Rect(shared.screen_width/2.67 - (215/2), shared.screen_height / 16, 205, 45)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.clear_node_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.clear_node_button)
        self.clear_node_button_text = self.game_and_home_screen_button_font.render('Clear Nodes', True, (0,0,0))
        self.clear_node_button_text_rect = self.clear_node_button_text.get_rect()
        self.clear_node_button_text_rect.center=self.clear_node_button.center
        self.screen.blit(self.clear_node_button_text, self.clear_node_button_text_rect)

    def create_clear_nodes_button(self):
        self.clear_node_button_shade = shared.pygame.Rect(shared.screen_width/2.67 - (215/2), shared.screen_height / 16, 225, 65)
        self.clear_node_button = shared.pygame.Rect(shared.screen_width/2.67 - (215/2), shared.screen_height / 16, 215, 55)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.clear_node_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.clear_node_button)
        self.clear_node_button_text = self.game_and_home_screen_button_font.render('Clear Nodes', True, (0,0,0))
        self.clear_node_button_text_rect = self.clear_node_button_text.get_rect()
        self.clear_node_button_text_rect.center=self.clear_node_button.center
        self.screen.blit(self.clear_node_button_text, self.clear_node_button_text_rect)

    def shrink_add_node_button(self):
        self.add_node_button_shade = shared.pygame.Rect(shared.screen_width/8 - (215/2), shared.screen_height / 16, 215, 55)
        self.add_node_button = shared.pygame.Rect(shared.screen_width/8 - (215/2), shared.screen_height / 16, 205, 45)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.add_node_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.add_node_button)
        self.add_node_button_text = self.game_and_home_screen_button_font.render('Add Node', True, (0,0,0))
        self.add_node_button_text_rect = self.add_node_button_text.get_rect()
        self.add_node_button_text_rect.center=self.add_node_button.center
        self.screen.blit(self.add_node_button_text, self.add_node_button_text_rect)

    def create_add_node_button(self):
        self.add_node_button_shade = shared.pygame.Rect(shared.screen_width/8 - (215/2), shared.screen_height / 16, 225, 65)
        self.add_node_button = shared.pygame.Rect(shared.screen_width/8 - (215/2), shared.screen_height / 16, 215, 55)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.add_node_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.add_node_button)
        self.add_node_button_text = self.game_and_home_screen_button_font.render('Add Node', True, (0,0,0))
        self.add_node_button_text_rect = self.add_node_button_text.get_rect()
        self.add_node_button_text_rect.center=self.add_node_button.center
        self.screen.blit(self.add_node_button_text, self.add_node_button_text_rect)

    def shrink_game_start_button(self):
        self.game_start_button_shade = shared.pygame.Rect(shared.screen_width/1.6 - (215/2), shared.screen_height / 16, 215, 55)
        self.game_start_button = shared.pygame.Rect(shared.screen_width/1.6 - (215/2), shared.screen_height / 16, 205, 45)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.game_start_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.game_start_button)
        self.game_start_button_text = self.game_and_home_screen_button_font.render('Start', True, (0,0,0))
        self.game_start_button_text_rect = self.game_start_button_text.get_rect()
        self.game_start_button_text_rect.center=self.game_start_button.center
        self.screen.blit(self.game_start_button_text, self.game_start_button_text_rect)

    def create_game_start_button(self):
        #Start buttons
        self.game_start_button_shade = shared.pygame.Rect(shared.screen_width/1.6 - (215/2), shared.screen_height / 16, 225, 65)
        self.game_start_button = shared.pygame.Rect(shared.screen_width/1.6 - (215/2), shared.screen_height / 16, 215, 55)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.game_start_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.game_start_button)
        self.game_start_button_text = self.game_and_home_screen_button_font.render('Start', True, (0,0,0))
        self.game_start_button_text_rect = self.game_start_button_text.get_rect()
        self.game_start_button_text_rect.center=self.game_start_button.center
        self.screen.blit(self.game_start_button_text, self.game_start_button_text_rect)

    def shrink_game_return_button(self):
        self.game_return_button_shade = shared.pygame.Rect(shared.screen_width/1.15 - (215/2), shared.screen_height / 16, 215, 55)
        self.game_return_button = shared.pygame.Rect(shared.screen_width/1.15 - (215/2), shared.screen_height / 16, 205, 45)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.game_return_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.game_return_button)
        self.game_return_button_text = self.game_and_home_screen_button_font.render('Return', True, (0,0,0))
        self.game_return_button_text_rect = self.game_return_button_text.get_rect()
        self.game_return_button_text_rect.center=self.game_return_button.center
        self.screen.blit(self.game_return_button_text, self.game_return_button_text_rect)

    def create_game_return_button(self):
        #return buttons
        self.game_return_button_shade = shared.pygame.Rect(shared.screen_width/1.15 - (215/2), shared.screen_height / 16, 225, 65)
        self.game_return_button = shared.pygame.Rect(shared.screen_width/1.15 - (215/2), shared.screen_height / 16, 215, 55)
        shared.pygame.draw.rect(self.screen, (0,0,0), self.game_return_button_shade)
        shared.pygame.draw.rect(self.screen, shared.light_green, self.game_return_button)
        self.game_return_button_text = self.game_and_home_screen_button_font.render('Return', True, (0,0,0))
        self.game_return_button_text_rect = self.game_return_button_text.get_rect()
        self.game_return_button_text_rect.center=self.game_return_button.center
        self.screen.blit(self.game_return_button_text, self.game_return_button_text_rect)
