from PyQt6.QtWidgets import QMainWindow, QApplication
from gallowsdir.gallows_ui import Ui_Form
from PGWigets import *
import sys
import random
from gallowsdir.gallows_words import *
import pygame
global theme
global difficulty

class GallowsMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Настройки виселицы')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        global theme
        theme = self.theme_comboBox.currentText()
        global difficulty
        difficulty = self.difficulty_comboBox.currentIndex()
        self.close()





def gallows_menu():
    app = QApplication(sys.argv)
    gallows_menu = GallowsMenu()
    gallows_menu.show()
    app.exec()


def generate_word(theme, difficulty):
    word = ''
    if theme == 'Случайная':
        theme = random.choice(['Животные', 'Природа', 'Еда', 'Страны'])
    d = {'Природа': nature,
         'Еда': food,
         'Страны': countries,
         'Животные': animals}
    if difficulty == 0:
        word = random.choice(list(filter(lambda x: 3 <= len(x) <= 5, d.get(theme))))
    elif difficulty == 1:
        word = random.choice(list(filter(lambda x: 6 <= len(x) <= 8, d.get(theme))))
    elif difficulty == 2:
        print((list(filter(lambda x: 9 <= len(x) <= 11, d.get(theme)))))
        word = random.choice(list(filter(lambda x: 9 <= len(x) <= 11, d.get(theme))))
    return word


def gallows_run(screen):
    def back():
        global run
        run = False

    gallows_menu()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    word = generate_word(theme, difficulty)

    L = []
    all_sprites = pygame.sprite.Group()

    btn_back = Button(all_sprites, back, (10, 540, 150, 50), 'В меню', body_color=(220, 255, 180),
                      shadow_color=(200, 235, 160), line_color=(180, 200, 140))
    theme_label = Label(all_sprites, f'Тема: {theme}', (190, 10), 80, (0, 0, 0))
    letter_label = Label(all_sprites, 'Введите букву:', (10, 80), 60, 'black')
    char_lineedit = LineEdit(all_sprites, word, (350, 80), 60, 1)
    text = ''
    global run
    run = True
    while run:
        screen.fill(pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            all_sprites.update(event)

        all_sprites.draw(screen)

        pygame.display.update()
        pygame.display.flip()
