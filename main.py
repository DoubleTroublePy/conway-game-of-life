from ConwayClass import Grid, Option
import pygame_menu
import pygame

if __name__ == '__main__':
    def start_the_game():
        name = name_input.get_value()
        g = Grid(int(name))
        g.run()

    surface = pygame.display.set_mode((400, 300))

    menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_DARK)

    menu.add.button('Play', start_the_game)
    name_input = menu.add.text_input('Dimension :', default='50')
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)