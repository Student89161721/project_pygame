from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit
from gallows_ui import Ui_Form
from PGWigets import *
import sys


class GallowsMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Настройки виселицы')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.close()
        theme = self.theme_comboBox.currentText()
        difficulty = self.difficulty_comboBox.currentText()
        Gallows(theme, difficulty)


# def gallows_run(screen):
#     def back():
#         global run
#         run = False
#
#     global run
#     run = True
#     all_sprites = pygame.sprite.Group()
#
#     btn_back = Button(all_sprites, back, (10, 365, 150, 25), 'В меню', body_color=(220, 255, 180),
#                       shadow_color=(200, 235, 160), line_color=(180, 200, 140))
#     label = Label(all_sprites, 'Тут будет виселица', (10, 10), 30, 50)
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             all_sprites.update(event)
#         screen.fill((255, 255, 255))
#         all_sprites.draw(screen)
#         pygame.display.flip()


class Gallows:
    def __init__(self, theme, difficulty):
        pygame.init()
        self.theme = theme
        self.difficulty = difficulty
        self.run()

    def run(self):
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        all_sprites = pygame.sprite.Group()
        running = True
        while running:
            screen.fill(pygame.Color('white'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                all_sprites.update(event)
            all_sprites.draw(screen)
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Gallows_menu = GallowsMenu()
    Gallows_menu.show()
    app.exec()