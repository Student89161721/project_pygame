from PyQt6.QtWidgets import QMainWindow, QApplication
from gallows_ui import Ui_Form
from PGWigets import *
from time import time
import sys
import random
from gallows_words import *
import pygame



class GallowsMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Настройки виселицы')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.close()
        theme = self.theme_comboBox.currentText()
        difficulty = self.difficulty_comboBox.currentIndex()
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
        self.L = []
        if self.theme == 'Случайная':
            self.theme = random.choice(['Животные', 'Природа', 'Еда', 'Страны'])
        self.word = ''
        self.difficulty = difficulty
        self.run()

    def run(self):
        pygame.init()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        all_sprites = pygame.sprite.Group()

        btn_back = Button(all_sprites, None, (10, 540, 150, 50), 'В меню', body_color=(220, 255, 180),
                          shadow_color=(200, 235, 160), line_color=(180, 200, 140))
        theme_label = Label(all_sprites, f'Тема: {self.theme}', (190, 10), 80, (0, 0, 0))
        letter_label = Label(all_sprites, 'Введите букву:', (10, 80), 60, 'black')

        text = ''
        font = pygame.font.SysFont('', 60)
        img = font.render(text, True, 'black')

        rect = img.get_rect()
        rect.topleft = (350, 80)
        cursor = pygame.Rect(rect.topright, (3, rect.height))
        self.word = self.generate_word()
        running = True
        # выход из игры можно сделать путём назначения на кнопку в меню функции, приравнивающей  running  к false
        # Лучше тогда на крестик поставить краш проги, а не в конец цикла
        # lineedit надо запихнуть в класс в PGWigets
        while running:
            screen.fill(pygame.Color('white'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text = ''
                    else:
                        if len(text) == 0:
                            if event.unicode in 'йцукенгшщзхъфывапролджэячсмитьбюё':
                                text = event.unicode
                    if event.key == 13:  # Если нажат enter
                        if text:
                            if text in self.word:
                                print('yes')
                            else:
                                if text not in self.L:
                                    self.L.append(text)
                                    letters = Label(all_sprites, f'Данных букв нет в слове: {", ".join(self.L)}',
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
        pygame.quit()

    def generate_word(self):
        d = {'Природа': nature,
             'Еда': food,
             'Страны': countries,
             'Животные': animals}
        if self.difficulty == 0:
            self.word = random.choice(list(filter(lambda x: 3 <= len(x) <= 5, d.get(self.theme))))
        elif self.difficulty == 1:
            self.word = random.choice(list(filter(lambda x: 6 <= len(x) <= 8, d.get(self.theme))))
        elif self.difficulty == 2:
            print((list(filter(lambda x: 9 <= len(x) <= 11, d.get(self.theme)))))
            self.word = random.choice(list(filter(lambda x: 9 <= len(x) <= 11, d.get(self.theme))))
        return self.word

# это не нужно
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Gallows_menu = GallowsMenu()
    Gallows_menu.show()
    app.exec()