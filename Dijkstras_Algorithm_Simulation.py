#Author: Kelby Amandy
#Date: 5/8/2023

import dijkstra_home_screen, dijkstra_info_screen, dijkstra_setup_screen
import import_handler as shared

HomeScreen = dijkstra_home_screen.HomeScreen()
InfoScreen = dijkstra_info_screen.InfoScreen()
SetupScreen = dijkstra_setup_screen.SetupScreen()


def main():
    current_screen = HomeScreen
    while True:

        #Drawing and updating screens
        current_screen.draw()
        current_screen.update()

        #Handling events for each screen
        for event in shared.pygame.event.get():
            current_screen.handle_event(event)

        # #Drawing and updating screens
        # current_screen.draw()
        # current_screen.update()
        
        #Changing screens
        if current_screen.is_done() == True:
            next_screen = current_screen.next_screen
            if next_screen == 'info_screen':
                current_screen = InfoScreen
                current_screen.screen_done = False
            elif next_screen == 'home_screen':
                current_screen = HomeScreen
                current_screen.screen_done = False
            elif next_screen == 'setup_screen':
                current_screen = SetupScreen
                current_screen.screen_done = False

        shared.pygame.display.flip()
        shared.clock.tick(60)

if __name__ == '__main__':
    main()

