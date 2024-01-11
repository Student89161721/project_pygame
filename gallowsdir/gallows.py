from PyQt6.QtWidgets import QMainWindow, QApplication
from gallowsdir.gallows_ui import Ui_Form
from PGWigets import *
import random
from math import pi
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

    all_sprites = pygame.sprite.Group()

    btn_back = Button(all_sprites, back, (10, 540, 150, 50), 'В меню', body_color=(220, 255, 180),
                      shadow_color=(200, 235, 160), line_color=(180, 200, 140))
    theme_label = Label(all_sprites, f'Тема: {theme}', (190, 10), 80, (0, 0, 0))
    letter_label = Label(all_sprites, 'Введите букву:', (10, 80), 60, 'black')
    # char_lineedit = LineEdit(all_sprites, word, (350, 80), 60, 1)
    L = []

    text = ''
    font = pygame.font.SysFont('', 60)
    image = font.render(text, True, 'black')

    rect = image.get_rect()
    rect.topleft = (350, 80)
    cursor = pygame.Rect(rect.topright, (3, rect.height))
    text = ''

    global run
    run = True
    global count
    count = 0
    while run:
        screen.fill(pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
                                count += 1

                        text = ''

                image = font.render(text, True, 'black')
                rect.size = image.get_size()
                cursor.topleft = rect.topright

        draw_hangman(screen)
        all_sprites.draw(screen)
        screen.blit(image, rect)
        if time() % 1 > 0.5:
            pygame.draw.rect(screen, 'black', cursor)
        pygame.display.update()
        pygame.display.flip()


def draw_hangman(screen):
    if count > 0:
        pygame.draw.line(screen, 'black', (330, 415), (330, 170), 7)
        pygame.draw.line(screen, 'black', (280, 415), (380, 415), 7)
    if count > 1:
        pygame.draw.line(screen, 'black', (327, 170), (500, 170), 7)
        pygame.draw.line(screen, 'black', (400, 170), (327, 238), 7)
    cx, cy, r = 450, 250, 30
    if count > 2:
        pygame.draw.line(screen, 'black', (cx, cy - 80), (cx, cy - r), 3)
        pygame.draw.circle(screen, 'black', (cx, cy), r, 2)
        pygame.draw.arc(screen, 'black', (435, 262, 30, 10), 0, pi, 2)
        x1, y1, x2, y2, sh = 432, 234, 443, 245, 23
        pygame.draw.line(screen, 'black', (x1, y1), (x2, y2), 2)
        pygame.draw.line(screen, 'black', (x2, y1), (x1, y2), 2)
        pygame.draw.line(screen, 'black', (x1 + sh, y1), (x2 + sh, y2), 2)
        pygame.draw.line(screen, 'black', (x2 + sh, y1), (x1 + sh, y2), 2)
    if count > 3:
        pygame.draw.line(screen, 'black', (cx, cy + r), (cx, cy + 100), 2)
    x1, x2, y1, y2, sh = 425, 475, 330, 305, 45
    if count > 4:
        pygame.draw.lines(screen, 'black', False, [(x1, y1), (cx, y2), [x2, y1]], 2)
    if count > 5:
        pygame.draw.lines(screen, 'black', False, [(x1, y1 + sh), (cx, y2 + sh), [x2, y1 + sh]], 2)