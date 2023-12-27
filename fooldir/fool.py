import pygame.transform
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit
from fooldir.fool_menu_ui import Ui_Form
from PyQt6 import QtCore
from PGWigets import *
from random import randint

CARD_SIZE = (85, 125)
HAND_COORDS = (100, 330)
BOT_COORDS = (100, 10)
PACK_COORDS = (10, 150)
HAND_SIZE = 250
HAND_STEP = 50
WIDTH, HEIGHT = 500, 500


class FoolMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Настройки дурака')
        self.pushButton.clicked.connect(self.close)


class Card(pygame.sprite.Sprite):
    def __init__(self, group, cards, sen, lear):
        super().__init__(group)
        self.cross = False
        self.click = False
        self.mouse_pos = (0, 0)
        self.state = ''
        self.max_size, self.min_size = CARD_SIZE, (CARD_SIZE[0] // 2, CARD_SIZE[1] // 2)
        self.lear, self.sen = lear, sen # масть от 1 до 4, старшинство от 1 до 13
        self.other_image = cards[4]
        self.image = cards[lear - 1][sen - 1]
        self.rect = pygame.Rect(0, 0, *CARD_SIZE)

    def update(self, event):
        if self.state == 'player':
            if event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
                if (self.rect.x + self.rect.width >= event.pos[0] >= self.rect.x and
                        self.rect.y + self.rect.height >= event.pos[1] >= self.rect.y):
                    self.cross = True
                else:
                    self.cross = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.click = False

    def draw(self, coords):
        self.rect.x, self.rect.y = coords

    def flip(self):
        self.image, self.other_image = self.other_image, self.image

    def set_state(self, state):
        if self.state == 'pack_end':
            self.image = pygame.transform.rotate(self.image, -90)
            self.rect = self.image.get_rect()
        if state == 'pack_end':
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect()
        if self.state == 'pack' or state == 'pack':
            self.flip()
        if self.state == 'bot' or state == 'bot':
            self.flip()
        if self.state == 'field' or self.state == 'field':
            self.max_size, self.min_size = self.min_size, self.max_size
            self.image = pygame.transform.scale(self.image, self.max_size)
        self.state = state


class Player:
    def __init__(self):
        self.hand = []

    def draw(self):
        step = HAND_STEP
        coords = HAND_COORDS
        if step * len(self.hand) <= HAND_SIZE:
            coords = (HAND_COORDS[0] + (HAND_SIZE - (step * len(self.hand))) // 2, coords[1])
        else:
            step = HAND_SIZE // len(self.hand)
        cross = True
        for i in range(len(self.hand)):
            if self.hand[i].cross and cross:
                cross = False
                if self.hand[i].click:
                    pos = self.hand[i].mouse_pos
                    self.hand[i].draw((pos[0] - (CARD_SIZE[0] // 2), pos[1] - (CARD_SIZE[1] // 2)))
                else:
                    self.hand[i].draw((coords[0] + (step * i), coords[1] - 30))
            else:
                self.hand[i].draw((coords[0] + (step * i), coords[1]))

    def add_to_hand(self, *cards):
        for elem in cards:
            elem.set_state('player')
        self.hand.extend(cards)


class Bot:
    def __init__(self):
        self.hand = []

    def draw(self):
        step = HAND_STEP
        coords = BOT_COORDS
        if step * len(self.hand) <= HAND_SIZE:
            coords = (HAND_COORDS[0] + (HAND_SIZE - (step * len(self.hand))) // 2, coords[1])
        else:
            step = HAND_SIZE // len(self.hand)
        cross = True
        for i in range(len(self.hand)):
            if self.hand[i].cross and cross:
                cross = False
                self.hand[i].draw((coords[0] + (step * i), coords[1] - 30))
            else:
                self.hand[i].draw((coords[0] + (step * i), coords[1]))

    def add_to_hand(self, *cards):
        for elem in cards:
            elem.set_state('bot')
        self.hand.extend(cards)


class Pack:
    def __init__(self, pack):
        self.pack = pack
        self.pack[0].set_state('pack_end')
        self.pack[-1].set_state('pack')

    def draw(self):
        if self.pack:
            self.pack[0].draw((PACK_COORDS[0] * 1.5, PACK_COORDS[1] * 1.2))
            if len(self.pack) > 1:
                self.pack[-1].draw(PACK_COORDS)


def fool_run(screen):
    def back():
        global run
        run = False

    global run
    run = True
    cards = [[load_image('fooldir/cards.png', -1).subsurface(pygame.Rect(5 + CARD_SIZE[0] * i, CARD_SIZE[1] * j,
                                                                         *CARD_SIZE)) for i in range(13)] for j in range(4)]
    shirt = load_image('fooldir/shirt.png', -1).subsurface(pygame.Rect(0, 0, *CARD_SIZE))
    cards.append(shirt)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    all_sprites = pygame.sprite.Group()

    btn_back = Button(all_sprites, back, (10, 465, 150, 25), 'В меню', body_color=(220, 255, 180),
                      shadow_color=(200, 235, 160), line_color=(180, 200, 140))
    player = Player()
    for i in range(1, 7):
        card = Card(all_sprites, cards, i, randint(1, 4))
        player.add_to_hand(card)
    bot = Bot()
    for i in range(1, 7):
        card = Card(all_sprites, cards, i, randint(1, 4))
        bot.add_to_hand(card)
    pack = Pack([Card(all_sprites, cards, 1, 2), Card(all_sprites, cards, 2, 2)])
    fps = 60
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            all_sprites.update(event)
        screen.fill((100, 150, 200))
        all_sprites.draw(screen)
        player.draw()
        pack.draw()
        bot.draw()
        clock.tick(fps)
        pygame.display.flip()
