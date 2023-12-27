from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit
from soldir.solitaire_ui import Ui_Form
from PGWigets import *



class SolitaireMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Настройки косынки')
        self.play_pushButton.clicked.connect(self.close)


def solitaire_run(screen):
    def back():
        global run
        run = False

    global run
    run = True
    all_sprites = pygame.sprite.Group()

    btn_back = Button(all_sprites, back, (10, 365, 150, 25), 'В меню', body_color=(220, 255, 180),
                      shadow_color=(200, 235, 160), line_color=(180, 200, 140))
    label = Label(all_sprites, 'Тут будет косынка', (10, 10), 30, 50)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            all_sprites.update(event)
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()