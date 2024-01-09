from PyQt6.QtWidgets import QMainWindow, QApplication
from gallowsdir.gallows_ui import Ui_Form
from PGWigets import *
from time import time
import sys
import random
from gallowsdir.gallows_words import *
import pygame



class GallowsMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Настройки виселицы')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.theme = self.theme_comboBox.currentText()
        self.difficulty = self.difficulty_comboBox.currentIndex()
        self.close()

    def get_theme(self):
        return self.theme

    def get_difficulty(self):
        return self.difficulty


def gallows_menu():
    app = QApplication(sys.argv)
    gallows_menu = GallowsMenu()
    gallows_menu.show()
    app.exec()


def generate_word(theme, difficulty):
    word = ''
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


# def __init__(self, theme, difficulty):
#     pygame.init()
#     self.theme = theme
#     self.L = []
#     if self.theme == 'Случайная':
#         self.theme = random.choice(['Животные', 'Природа', 'Еда', 'Страны'])
#     self.word = ''
#     self.difficulty = difficulty
#     self.run()




# def run(self):

#     all_sprites = pygame.sprite.Group()
#     def back():
#         global running
#         running = False


def gallows_run(screen):
    def back():
        global run
        run = False

    gallows_menu()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    theme = 'Случайная'
    difficulty = 0
    L = []
    if theme == 'Случайная':
        theme = random.choice(['Животные', 'Природа', 'Еда', 'Страны'])
    all_sprites = pygame.sprite.Group()

    btn_back = Button(all_sprites, back, (10, 540, 150, 50), 'В меню', body_color=(220, 255, 180),
                      shadow_color=(200, 235, 160), line_color=(180, 200, 140))
    theme_label = Label(all_sprites, f'Тема: {theme}', (190, 10), 80, (0, 0, 0))
    letter_label = Label(all_sprites, 'Введите букву:', (10, 80), 60, 'black')

    text = ''
    font = pygame.font.SysFont('', 60)
    img = font.render(text, True, 'black')

    rect = img.get_rect()
    rect.topleft = (350, 80)
    cursor = pygame.Rect(rect.topright, (3, rect.height))
    word = generate_word(theme, difficulty)
    global run
    run = True
    while run:
        screen.fill(pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            all_sprites.update(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = ''
                else:
                    if len(text) == 0:
                        if event.unicode in 'йцукенгшщзхъфывапролджэячсмитьбюё':
                            text = event.unicode
                if event.key == 13:  # Если нажат enter
                    if text:
                        if text in word:
                            print('yes')
                        else:
                            if text not in L:
                                L.append(text)
                                letters = Label(all_sprites, f'Данных букв нет в слове: {", ".join(L)}',
                                                (10, 130), 30, (255, 0, 0))

                        text = ''

                img = font.render(text, True, 'black')
                rect.size = img.get_size()
                cursor.topleft = rect.topright

        all_sprites.draw(screen)
        screen.blit(img, rect)
        if time() % 1 > 0.5:
            pygame.draw.rect(screen, 'black', cursor)
        pygame.display.update()
        pygame.display.flip()
