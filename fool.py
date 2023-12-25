from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit
from fool_menu_ui import Ui_Form
from PyQt6 import QtCore
from PGWigets import *



class FoolMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Настройки дурака')
        self.pushButton.clicked.connect(self.close)


def fool_run(screen):
    def back():
        global run
        run = False

    global run
    run = True
    all_sprites = pygame.sprite.Group()

    btn_back = Button(all_sprites, back, (10, 365, 150, 25), 'В меню', body_color=(220, 255, 180),
                      shadow_color=(200, 235, 160), line_color=(180, 200, 140))
    label = Label(all_sprites, 'Тут будет дурак', (10, 10), 30, 50)
    le = LineEdit(all_sprites, back, (10, 100, 150, 25), body_color=(220, 220, 220), line_color=(150, 150, 150),)

    fps = 60
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            all_sprites.update(event)
        le.draw()
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()