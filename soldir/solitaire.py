from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit
from soldir.solitaire_ui import Ui_Form
from PGWigets import *
from random import randint, shuffle

WIDTH, HEIGHT = 600, 600
CARD_SIZE = (85, 125)
FIELD_COORDS = (0, 150)
FIELD_STEP = 30
PACK_COORDS = (400, 10)


class SolitaireMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Настройки косынки')
        self.play_pushButton.clicked.connect(self.close)


class Card(pygame.sprite.Sprite):
    def __init__(self, group, cards, sen, lear):
        super().__init__(group)
        self.group = group
        self.cross = False
        self.click = False
        self.in_field = False
        self.can_move = False
        self.field_pos = 0
        self.mouse_pos = (0, 0)
        self.state = ''
        self.size_1, self.size_2 = CARD_SIZE, (CARD_SIZE[0] * 0.8, CARD_SIZE[1] * 0.8)
        self.lear, self.sen = lear, sen # масть от 1 до 4, старшинство от 1 до 13
        self.other_image = cards[4]
        self.image = cards[lear - 1][sen - 1]
        self.rect = pygame.Rect(0, 0, *CARD_SIZE)

    def __repr__(self):
        return f'{self.sen} {self.lear}'

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.mouse_pos = event.pos
            if (self.rect.x + self.rect.width >= event.pos[0] >= self.rect.x and
                    self.rect.y + self.rect.height >= event.pos[1] >= self.rect.y):
                self.cross = True
            else:
                self.cross = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.cross:
                self.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.click:
                    if self.mouse_pos[0] >= FIELD_COORDS[0] and self.mouse_pos[1] >= FIELD_COORDS[1]:
                        self.field_pos = self.mouse_pos[0] // CARD_SIZE[0]
                        self.in_field = True
                    self.click = False

    def draw(self, coords):
        self.rect.x, self.rect.y = coords

    def flip(self):
        self.image, self.other_image = self.other_image, self.image
        self.rect = self.image.get_rect()

    def set_state(self, state):
        self.state = state


class Field:
    def __init__(self, cards):
        self.cards = [[] for _ in range(7)]
        self.put = False
        for i in range(7):
            for j in range(i + 1):
                if cards:
                    self.cards[i].append(cards.pop())
                    self.cards[i][-1].group.move_to_front(self.cards[i][-1])
                    if j != i:
                        self.cards[i][-1].flip()
                    else:
                        self.cards[i][-1].can_move = True
        self.home = [[] for _ in range(4)]

    def add(self, card, pos):
        if self.cards[pos]:
            if self.cards[pos][-1].sen - card.sen == 1 and abs(self.cards[pos][-1].lear - card.lear) > 1:
                self.cards[pos].append(card)
                return True
            else:
                return False
        elif card.sen == 13:
            self.cards[pos].append(card)
            return True
        else:
            return False


    def draw(self):
        cross = True
        for i in range(len(self.cards)):
            for j in range(len(self.cards[i])):
                if len(self.cards[i]) > j:
                    self.cards[i][j].draw((FIELD_COORDS[0] + (CARD_SIZE[0] * i), FIELD_COORDS[1] + (FIELD_STEP * j)))
                    if len(self.cards[i]) > j:
                        if self.cards[i][j].cross and cross:
                            cross = False
                            if self.cards[i][j].click and self.cards[i][j].can_move:
                                pos = self.cards[i][j].mouse_pos
                                self.cards[i][j].draw((pos[0] - (CARD_SIZE[0] // 2), pos[1] - (CARD_SIZE[1] // 2)))
                                self.cards[i][j].group.move_to_front(self.cards[i][j])
                            if self.cards[i][j].in_field:
                                self.cards[i][j].in_field = False
                                if self.cards[self.cards[i][j].field_pos]:
                                    card = self.cards[self.cards[i][j].field_pos][-1]
                                    if card.sen - self.cards[i][j].sen == 1 and abs(card.lear - self.cards[i][j].lear) > 1:
                                        self.cards[self.cards[i][j].field_pos].append(self.cards[i].pop(j))
                                        if self.cards[i]:
                                            self.cards[i][-1].flip()
                                            self.cards[i][-1].can_move = True
                                else:
                                    if self.cards[i][j].sen == 13:
                                        self.cards[self.cards[i][j].field_pos].append(self.cards[i].pop(j))
                                        if self.cards[i]:
                                            self.cards[i][-1].flip()
                                            self.cards[i][-1].can_move = True


class Pack:
    def __init__(self, field, cards):
        self.cards = cards
        self.field = field
        for elem in self.cards:
            elem.flip()
        self.cards_open = []

    def draw(self):
        for elem in self.cards:
            elem.draw(PACK_COORDS)
        cross = True
        for elem in self.cards_open:
            elem.draw((PACK_COORDS[0] + CARD_SIZE[0], PACK_COORDS[1]))
            if elem.cross and cross:
                cross = False
                if elem.click:
                    pos = elem.mouse_pos
                    elem.draw((pos[0] - (CARD_SIZE[0] // 2), pos[1] - (CARD_SIZE[1] // 2)))
                if elem.in_field:
                    if self.field.add(elem, elem.field_pos):
                        del self.cards_open[self.cards_open.index(elem)]


    def open(self):
        if self.cards:
            self.cards_open.insert(0, self.cards.pop())
            self.cards_open[0].flip()
            self.cards_open[0].group.move_to_front(self.cards_open[0])
        elif self.cards_open:
            self.cards, self.cards_open = self.cards_open, self.cards
            for elem in self.cards:
                elem.flip()


def solitaire_run(screen):
    def back():
        global run
        run = False

    global run
    run = True
    all_sprites = pygame.sprite.LayeredUpdates()

    cards = [[load_image('fooldir/cards.png', -1).subsurface(pygame.Rect(5 + CARD_SIZE[0] * i, CARD_SIZE[1] * j, *CARD_SIZE)) for i in range(13)] for j in range(4)]
    shirt = load_image('fooldir/shirt.png', -1).subsurface(pygame.Rect(0, 0, *CARD_SIZE))
    cards.append(shirt)
    cards_array = [(i % 13 + 1, i // 13 + 1) for i in range(52)]
    shuffle(cards_array)

    btn_back = Button(all_sprites, back, (10, 565, 150, 25), 'В меню', body_color=(220, 255, 180),
                      shadow_color=(200, 235, 160), line_color=(180, 200, 140))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    field = Field([Card(all_sprites, cards, *elem) for elem in cards_array[:28]])
    pack = Pack(field, [Card(all_sprites, cards, *elem) for elem in cards_array[28:]])

    cross = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                if (PACK_COORDS[0] + CARD_SIZE[0] >= event.pos[0] >= PACK_COORDS[0] and
                        PACK_COORDS[1] + CARD_SIZE[1] >= event.pos[1] >= PACK_COORDS[1]):
                    cross = True
                else:
                    cross = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and cross:
                    pack.open()
            all_sprites.update(event)
        pack.draw()
        field.draw()
        screen.fill((100, 150, 200))
        all_sprites.draw(screen)
        pygame.display.flip()