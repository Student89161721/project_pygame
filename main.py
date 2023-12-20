import sys
import pygame
from PyQt6.QtWidgets import QApplication

from reg_login import RegistrationWidget, LoginWidget
from fool import FoolMenu
from PGWigets import *

WIDTH, HEIGHT = 400, 400

all_sprites = pygame.sprite.Group()


def login():
    app = QApplication(sys.argv)
    log = LoginWidget()
    log.show()
    app.exec()


def register():
    app = QApplication(sys.argv)
    reg = RegistrationWidget()
    reg.show()
    app.exec()


def fool_menu():
    app = QApplication(sys.argv)
    fool_menu = FoolMenu()
    fool_menu.show()
    app.exec()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

btn_log = Button(all_sprites, login, (10, 10, 150, 25), 'Войти', body_color=(255, 240, 150),
                 shadow_color=(235, 220, 130), line_color=(225, 200, 120))
btn_reg = Button(all_sprites, register, (170, 10, 150, 25), 'Зарегистрироваться', body_color=(255, 240, 150),
                 shadow_color=(235, 220, 130), line_color=(225, 200, 120))
btn_fool = Button(all_sprites, fool_menu, (10, 270, 170, 30), 'Дурак', body_color=(255, 240, 150),
                  shadow_color=(235, 220, 130), line_color=(225, 200, 120))
btn_gallows = Button(all_sprites, None, (10, 310, 170, 30), 'Виселица', body_color=(255, 240, 150),
                     shadow_color=(235, 220, 130), line_color=(225, 200, 120))
btn_solitaire = Button(all_sprites, None, (10, 350, 170, 30), 'Пасьянс', body_color=(255, 240, 150),
                       shadow_color=(235, 220, 130), line_color=(225, 200, 120))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
