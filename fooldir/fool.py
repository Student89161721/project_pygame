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
FIELD_POSES_SIZE = (80, 100)


class FoolMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Настройки дурака')
        self.pushButton.clicked.connect(self.close)


class Card(pygame.sprite.Sprite):
    def __init__(self, group, cards, sen, lear):
        super().__init__(group)
        self.group = group
        self.cross = False
        self.click = False
        self.in_field = False
        self.field_pos = 0
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
                        self.field_pos = 0
                        for elem in FIELD_POSES:
                            if (elem[0] <= event.pos[0] <= elem[0] + FIELD_POSES_SIZE[0] and
                                    elem[1] <= event.pos[1] <= elem[1] + FIELD_POSES_SIZE[1]):
                                break
                            self.field_pos += 1
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
        if self.state == 'field_up':
            self.size_1, self.size_2 = self.size_2, self.size_1
            self.image = pygame.transform.scale(self.image, self.size_1)
            self.image = pygame.transform.rotate(self.image, 30)
            self.rect = self.image.get_rect()
        if state == 'field_up':
            self.size_1, self.size_2 = self.size_2, self.size_1
            self.image = pygame.transform.scale(self.image, self.size_1)
            self.image = pygame.transform.rotate(self.image, -30)
            self.rect = self.image.get_rect()
            self.group.move_to_front(self)
        self.state = state


class Player:
    def __init__(self, field):
        self.hand = []
        self.field = field
        self.state = 'atk'

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
                if self.state == 'atk':
                    if self.field.add(elem):
                        del self.hand[self.hand.index(elem)]
                else:
                    if self.field.cover(elem, elem.field_pos):
                        del self.hand[self.hand.index(elem)]

    def add_to_hand(self, *cards):
        for elem in cards:
            elem.set_state('player')
        self.hand.extend(cards)


class Bot:
    def __init__(self, field):
        self.hand = []
        self.state = 'def'
        self.field = field

    def draw(self):
        self.update()
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

    def update(self):
        if self.state == 'def':
            cards = self.field.cards
            for i in range(len(cards)):
                if cards[i][0] and not cards[i][1]:
                    for e in sorted(self.hand, key=lambda x: x.sen):
                        if e.lear == cards[i][0].lear and e.sen > cards[i][0].sen:
                            self.field.cover(e, i)
                            del self.hand[self.hand.index(e)]
                            break
                    else:
                        if cards[i][0].lear != self.field.trump:
                            for e in sorted(self.hand, key=lambda x: x.sen):
                                if e.lear == self.field.trump:
                                    self.field.cover(e, i)
                                    del self.hand[self.hand.index(e)]
                                    break
                            else:
                                self.field.put_cards()
                        else:
                            self.field.put_cards()
                    for elem in self.hand:
                        elem.group.move_to_front(elem)
        else:
            for i in range(len(self.hand)):
                if self.field.add(self.hand[i]):
                    del self.hand[i]
                    break
            else:
                self.field.change_move()

    def add_to_hand(self, *cards):
        for elem in cards:
            elem.set_state('bot')
        self.hand.extend(cards)
        self.hand = sorted(self.hand, key=lambda x: x.sen)
        for elem in self.hand:
            elem.group.move_to_front(elem)


class Pack:
    def __init__(self, field, pack):
        self.pack = pack
        self.pack[0].set_state('pack_end')
        field.trump = self.pack[0].lear

        for elem in pack[1:]:
            elem.set_state('pack')

    def draw(self):
        if self.pack:
            for i in range(len(self.pack)):
                if i:
                    self.pack[i].draw(PACK_COORDS)
                else:
                    self.pack[i].draw((PACK_COORDS[0] * 1.5, PACK_COORDS[1] * 1.2))

    def put(self, number):
        return [self.pack.pop() for i in range(number) if len(self.pack) > i]


class Field:
    def __init__(self):
        self.cards = [[None, None] for _ in range(6)]
        self.cards_counter = 0
        self.trump = None
        self.move = False
        self.put = False

    def draw(self):
        for i in range(len(self.cards)):
            if self.cards[i][0]:
                self.cards[i][0].draw(FIELD_POSES[i])
            if self.cards[i][1]:
                self.cards[i][1].draw(FIELD_POSES[i])

    def add(self, card):
        if all([elem[0] is None for elem in self.cards]) or any([elem[0] and elem[0].sen == card.sen or elem[1]
                                                                 and elem[1].sen == card.sen for elem in self.cards]):
            card.set_state('field')
            self.cards[self.cards_counter][0] = card
            self.cards_counter += 1
            return True
        else:
            return False

    def cover(self, card, pos):
        if not self.cards[pos][0] is None and (card.lear == self.cards[pos][0].lear and card.sen >
                                               self.cards[pos][0].sen or card.lear != self.cards[pos][0].lear
                                               and card.lear == self.trump):
            card.set_state('field_up')
            self.cards[pos][1] = card
            return True
        else:
            return False

    def change_move(self):
        self.cards_counter = 0
        if any([not elem[0] is None and not elem[1] is None for elem in self.cards]):
            self.move = True

    def put_cards(self):
        self.cards_counter = 0
        if any([not elem[0] is None and elem[1] is None for elem in self.cards]):
            self.put = True

    def clear(self):
        for elem in self.cards:
            if not elem[0] is None:
                elem[0].kill()
            if not elem[1] is None:
                elem[1].kill()
        self.cards = [[None, None] for _ in range(6)]


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
    all_sprites = pygame.sprite.LayeredUpdates()
    cards_array = [(i % 13 + 1, i // 13 + 1) for i in range(52)]
    shuffle(cards_array)
    field = Field()
    player = Player(field)
    bot = Bot(field)
    for i in range(6):
        card = Card(all_sprites, cards, *cards_array.pop(i * 2))

        player.add_to_hand(card)
        card = Card(all_sprites, cards, *cards_array.pop(i * 2 + 1))
        bot.add_to_hand(card)
    pack = Pack(field, [Card(all_sprites, cards, *elem) for elem in cards_array])

    btn_back = Button(all_sprites, back, (10, 465, 150, 25), 'В меню', body_color=(220, 255, 180),
                      shadow_color=(200, 235, 160), line_color=(180, 200, 140))

    btn_bito = Button(all_sprites, field.change_move, (330, 465, 150, 25), 'Бито', body_color=(255, 255, 255),
                      shadow_color=(230, 230, 230), line_color=(100, 100, 100))
    fps = 60
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            all_sprites.update(event)
        if field.move:
            field.move = False
            field.clear()
            player.state, bot.state = bot.state, player.state
            bot.add_to_hand(*pack.put(6 - len(bot.hand)))
            player.add_to_hand(*pack.put(6 - len(bot.hand)))
            if player.state == 'atk':
                btn_bito.text = 'бито'
                btn_bito.func = field.change_move
            else:
                btn_bito.text = 'взять'
                btn_bito.func = field.put_cards
        elif field.put:
            field.put = False
            cards = []
            for i in range(len(field.cards)):
                for j in range(2):
                    if not field.cards[i][j] is None:
                        cards.append(field.cards[i][j])
                        field.cards[i][j] = None
            if player.state == 'atk':
                player.add_to_hand(*pack.put(6 - len(bot.hand)))
                bot.add_to_hand(*cards)
            else:
                bot.add_to_hand(*pack.put(6 - len(bot.hand)))
                player.add_to_hand(*cards)
        screen.fill((100, 150, 200))
        all_sprites.draw(screen)
        player.draw()
        pack.draw()
        bot.draw()
        field.draw()
        clock.tick(fps)
        pygame.display.flip()
