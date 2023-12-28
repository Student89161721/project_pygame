import pygame.transform
from PyQt6.QtWidgets import QMainWindow
from fooldir.fool_menu_ui import Ui_Form
from PGWigets import *
from random import randint, shuffle

CARD_SIZE = (85, 125)
HAND_COORDS = (100, 330)
BOT_COORDS = (100, 5)
PACK_COORDS = (0, 160)
HAND_SIZE = 250
HAND_STEP = 50
WIDTH, HEIGHT = 500, 500
FIELD_RECT = (100, 130, 300, 200)
FIELD_POSES = [(130, 150), (210, 150), (290, 150), (130, 250), (210, 250), (290, 250)]


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
        self.in_field = False
        self.mouse_pos = (0, 0)
        self.state = ''
        self.size_1, self.size_2 = CARD_SIZE, (CARD_SIZE[0] * 0.8, CARD_SIZE[1] * 0.8)
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
                    if (self.rect.x + self.rect.width >= event.pos[0] >=
                        self.rect.x and self.rect.y + self.rect.height >=
                        event.pos[1] >= self.rect.y) and self.click and \
                            (FIELD_RECT[0] <= self.rect.x <= FIELD_RECT[0]
                             + FIELD_RECT[2] and FIELD_RECT[1] <= self.rect.y <= FIELD_RECT[1] + FIELD_RECT[3]):
                        self.in_field = True
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
        if self.state == 'field' or state == 'field':
            self.size_1, self.size_2 = self.size_2, self.size_1
            self.image = pygame.transform.scale(self.image, self.size_1)
        self.state = state


class Player:
    def __init__(self, field):
        self.hand = []
        self.field = field

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
        for elem in self.hand:
            if elem.in_field:
                self.field.add(elem)
                del self.hand[self.hand.index(elem)]

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
        for elem in pack[1:]:
            elem.set_state('pack')

    def draw(self):
        if self.pack:
            for i in range(len(self.pack)):
                if i:
                    self.pack[i].draw(PACK_COORDS)
                else:
                    self.pack[i].draw((PACK_COORDS[0] * 1.5, PACK_COORDS[1] * 1.2))



class Field:
    def __init__(self):
        self.cards = []

    def draw(self):
        for i in range(len(self.cards)):
            self.cards[i].draw(FIELD_POSES[i])

    def add(self, card):
        card.set_state('field')
        self.cards.append(card)



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
    cards_array = [(i % 13 + 1, i // 13 + 1) for i in range(52)]
    shuffle(cards_array)
    field = Field()
    player = Player(field)
    bot = Bot()
    for i in range(6):
        card = Card(all_sprites, cards, *cards_array[i * 2])
        player.add_to_hand(card)
        card = Card(all_sprites, cards, *cards_array[i * 2 + 1])
        bot.add_to_hand(card)
    pack = Pack([Card(all_sprites, cards, *elem) for elem in cards_array])
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
        field.draw()
        clock.tick(fps)
        pygame.display.flip()
