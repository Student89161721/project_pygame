import pygame
import sys
import os

KEYBOARD = {pygame.K_q: 'й', pygame.K_w: 'ц', pygame.K_e: 'у', pygame.K_r: 'к', pygame.K_t: 'е', pygame.K_y: 'н',
            pygame.K_u: 'г', pygame.K_i: 'ш', pygame.K_o: 'щ', pygame.K_p: 'з', pygame.K_LEFTBRACKET: 'х',
            pygame.K_a: 'ф', pygame.K_s: 'ы', pygame.K_d: 'в', pygame.K_f: 'а', pygame.K_g: 'п', pygame.K_j: 'о',
            pygame.K_k: 'л', pygame.K_l: 'д', pygame.K_COLON: 'ж', pygame.K_QUOTEDBL: 'э', pygame.K_z: 'я',
            pygame.K_x: 'ч', pygame.K_c: 'с', pygame.K_v: 'м', pygame.K_b: 'и', pygame.K_n: 'т', pygame.K_m: 'ь',
            pygame.K_LESS: 'б', pygame.K_GREATER: 'ю', pygame.K_h: 'р'}


class Button(pygame.sprite.Sprite):
    def __init__(self, group, func, rect, text='', body_color=(255, 255, 150), shadow_color=(225, 225, 120),
                 line_color=(0, 0, 0), text_color=(0, 0, 0)):
        super().__init__(group)
        self.body_color, self.shadow_color, self.line_color, self.text_color = body_color, shadow_color, line_color,\
                                                                               text_color
        self.rect = pygame.Rect(rect)
        self.text = text
        self.cross = False
        self.func = func

        self.image = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, body_color, (0, 0, rect[2], rect[3]))
        pygame.draw.rect(self.image, line_color, (0, 0, rect[2], rect[3]), 1)
        self.draw_text()

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            if (self.rect.x + self.rect.width >= event.pos[0] >= self.rect.x and
                    self.rect.y + self.rect.height >= event.pos[1] >= self.rect.y):
                self.cross = True
                pygame.draw.rect(self.image, self.shadow_color, (0, 0, self.rect.width, self.rect.height))
                pygame.draw.rect(self.image, self.line_color, (0, 0, self.rect.width, self.rect.height), 1)
                self.draw_text()
            else:
                self.cross = False
                pygame.draw.rect(self.image, self.body_color, (0, 0, self.rect.width, self.rect.height))
                pygame.draw.rect(self.image, self.line_color, (0, 0, self.rect.width, self.rect.height), 1)
                self.draw_text()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.cross:
                self.func()

    def draw_text(self):
        font = pygame.font.Font(None, 20)
        text = font.render(self.text, True, self.text_color)
        x = self.rect.width // 2 - text.get_width() // 2
        y = self.rect.height // 2 - text.get_height() // 2
        self.image.blit(text, (x, y))


class Label(pygame.sprite.Sprite):
    def __init__(self, group, text, coords, size=20, text_color=(0, 0, 0)):
        super().__init__(group)
        font = pygame.font.Font(None, size)
        text = font.render(text, True, text_color)
        self.image = pygame.Surface((text.get_width(), text.get_height()), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(*coords, text.get_width(), text.get_height())
        self.image.blit(text, (0, 0))


class LineEdit(pygame.sprite.Sprite):
    def __init__(self, group, func, rect, max_leght=1,shadow_color=(225, 225, 120), body_color=(255, 255, 150),
                 line_color=(0, 0, 0), text_color=(0, 0, 0)):
        super().__init__(group)
        self.body_color, self.shadow_color, self.line_color, self.text_color = body_color, shadow_color, line_color,\
                                                                               text_color
        self.rect = pygame.Rect(rect)
        self.max_leght = max_leght
        self.text = ''
        self.text_end = 0
        self.clicked = False
        self.cross = False
        self.line = -1
        self.func = func

        self.image = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, body_color, (0, 0, rect[2], rect[3]))
        pygame.draw.rect(self.image, line_color, (0, 0, rect[2], rect[3]), 1)
        self.draw_text()

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            if (self.rect.x + self.rect.width >= event.pos[0] >= self.rect.x and
                    self.rect.y + self.rect.height >= event.pos[1] >= self.rect.y):
                self.cross = True
                self.draw_text()
            else:
                self.cross = False
                self.draw_text()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.cross:
                    self.clicked = True
                else:
                    self.clicked = False
        elif event.type == pygame.KEYDOWN:
            if self.clicked:
                if len(self.text) < self.max_leght:
                    if event.key in KEYBOARD:
                        self.text = self.text + KEYBOARD[event.key]
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

    def draw(self):
        if self.clicked:
            self.line += 1
            if self.line == 100:
                self.line = 0
        else:
            self.line = -1
        if not self.clicked:
            pygame.draw.rect(self.image, self.body_color, (0, 0, self.rect[2], self.rect[3]))
            pygame.draw.rect(self.image, self.line_color, (0, 0, self.rect[2], self.rect[3]), 1)
        if 0 <= self.line < 50:
            pygame.draw.line(self.image, self.text_color, (self.text_end + 2, 2), (self.text_end + 2, self.rect[3] - 4))
        else:
            pygame.draw.rect(self.image, self.body_color, (0, 0, self.rect[2], self.rect[3]))
            pygame.draw.rect(self.image, self.line_color, (0, 0, self.rect[2], self.rect[3]), 1)
        self.draw_text()

    def draw_text(self):
        font = pygame.font.Font(None, 20)
        text = font.render(self.text, True, self.text_color)
        x = 2
        y = self.rect.height // 2 - text.get_height() // 2
        self.text_end = text.get_width()
        self.image.blit(text, (x, y))


def load_image(name, colorkey=None):
    fullname = name
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

