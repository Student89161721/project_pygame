import pygame

# Класс вынесен в отделный файл, тк используется везде
# Кнопки пока что рисуются, потом сделаем картинками
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