from PyQt5.QtWidgets import QMainWindow, QApplication
from gallowsdir.gallows_ui import Ui_Form
from PGWigets import *
import random
from math import pi
import pygame
import sqlite3

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
        if theme == 'Случайная':
            theme = random.choice(['Животные', 'Природа', 'Еда', 'Страны'])
        global difficulty
        difficulty = self.difficulty_comboBox.currentIndex()
        self.close()


def gallows_menu():
    app = QApplication(sys.argv)
    gallows_menu = GallowsMenu()
    gallows_menu.show()
    app.exec()


def generate_word(theme, difficulty):
    con = sqlite3.connect("gallowsdir/database.db")
    cur = con.cursor()
    word = ''

    d = {'Природа': [elem[0] for elem in cur.execute("""SELECT word FROM words WHERE theme = 'nature'""").fetchall()],
         'Еда': [elem[0] for elem in cur.execute("""SELECT word FROM words WHERE theme = 'food'""").fetchall()],
         'Страны': [elem[0] for elem in cur.execute("""SELECT word FROM words WHERE theme = 'countries'""").fetchall()],
         'Животные': [elem[0] for elem in cur.execute("""SELECT word FROM words WHERE theme = 'animals'""").fetchall()]}
    con.close()
    if difficulty == 0:
        word = random.choice(list(filter(lambda x: 3 <= len(x) <= 5, d.get(theme))))
    elif difficulty == 1:
        word = random.choice(list(filter(lambda x: 6 <= len(x) <= 8, d.get(theme))))
    elif difficulty == 2:
        word = random.choice(list(filter(lambda x: 9 <= len(x) <= 11, d.get(theme))))
    return word


def gallows_run(screen):
    def back():
        pygame.mixer.pause()
        global run
        run = False

    gallows_menu()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    global theme
    word = generate_word(theme, difficulty)

    all_sprites = pygame.sprite.Group()
    global snd
    snd = True
    music = pygame.mixer.Sound('music.mp3')

    def sound():
        global snd
        if snd:
            music.play(loops=-1)
            btn_sound.body_color = (180, 215, 130)
            btn_sound.shadow_color = (220, 255, 180)
            btn_sound.text = 'Выключить звук'
            btn_sound.line_color = (220, 240, 180)
            snd = False
        else:
            pygame.mixer.pause()
            btn_sound.body_color = (220, 255, 180)
            btn_sound.shadow_color = (200, 235, 160)
            btn_sound.text = 'Включить звук'
            btn_sound.line_color = (180, 200, 140)
            snd = True

    btn_back = Button(all_sprites, back, (10, 540, 150, 50), 'В меню', body_color=(220, 255, 180),
                      shadow_color=(200, 235, 160), line_color=(180, 200, 140))
    btn_sound = Button(all_sprites, sound, (10, 475, 150, 50), 'Включить звук', body_color=(220, 255, 180),
                       shadow_color=(200, 235, 160), line_color=(180, 200, 140))

    theme_label = Label(all_sprites, f'Тема: {theme}', (190, 10), 80, (0, 0, 0))
    letter_label = Label(all_sprites, 'Введите букву:', (10, 80), 60, 'black')
    try_label = Label(all_sprites, 'Осталось попыток: 7',
                      (12, 120), 30, 'black')
    # char_lineedit = LineEdit(all_sprites, word, (350, 80), 60, 1)
    L = []

    text = ''
    font = pygame.font.SysFont('', 60)
    image = font.render(text, True, 'black')

    rect = image.get_rect()
    rect.topleft = (350, 80)
    cursor = pygame.Rect(rect.topright, (3, rect.height))
    text = ''
    word = word.lower()

    global run
    run = True
    global count
    count = 0

    while run:
        screen.fill(pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.pause()
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
                            for elem in symbol_coords(text, word):
                                Label(all_sprites, text, (elem, 430), 250, 'black')

                        else:
                            if text not in L:
                                L.append(text)
                                letters = Label(all_sprites, f'Данных букв нет в слове: {", ".join(L)}',
                                                (10, 140), 30, (255, 0, 0))
                                count += 1
                                try_label.kill()
                                try_label = Label(all_sprites, f'Осталось попыток: {7 - count}',
                                                  (12, 120),30, 'black')

                        text = ''

                image = font.render(text, True, 'black')
                rect.size = image.get_size()
                cursor.topleft = rect.topright

        draw_lines(word, screen)
        draw_hangman(screen)
        all_sprites.draw(screen)
        screen.blit(image, rect)
        if time() % 1 > 0.5:
            pygame.draw.rect(screen, 'black', cursor)
        if count == 7:
            return False
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


def draw_lines(word, screen):
    y = 580
    x1, x2 = 170, 770 + (10 * len(word))
    length = ((x2 - x1) - (10 * (len(word) - 1))) // len(word)
    for i in range(len(word)):
        pygame.draw.line(screen, 'black', (x1 + (length * i) + 10, y),
                         (x1 + (length * (i + 1)), y), 10)


def symbol_coords(symbol, word):
    indexes = [i for i, el in enumerate(word) if el == symbol]

    print(indexes)

    x1, x2 = 170, 770 + (10 * len(word))
    length = ((x2 - x1) - (10 * (len(word) - 1))) // len(word)
    print(length)
    print(word)
    font = pygame.font.SysFont('', 250)
    image = font.render(symbol, True, 'black')
    rect = image.get_rect()
    rect.topleft = (170, 430)
    print(rect.topleft)
    print(rect.topright)
    return [x1 + (el * length) + ((length - 100) // 2) for el in indexes]

