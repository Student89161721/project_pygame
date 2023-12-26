import sys
import pygame
from PyQt6.QtWidgets import QApplication

from reg_login import RegistrationWidget, LoginWidget
from fool import FoolMenu, fool_run
from gallows import GallowsMenu
from solitaire import SolitaireMenu, solitaire_run
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


def gallows_menu():
    app = QApplication(sys.argv)
    gallows_menu = GallowsMenu()
    gallows_menu.show()
    app.exec()


def solitaire_menu():
    app = QApplication(sys.argv)
    solitaire_menu = SolitaireMenu()
    solitaire_menu.show()
    app.exec()

def fool():
    fool_menu()
    fool_run(screen)


def gallows():
    gallows_menu()


def solitaire():
    solitaire_menu()
    solitaire_run(screen)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

btn_log = Button(all_sprites, login, (10, 10, 150, 25), 'Войти', body_color=(255, 240, 150),
                 shadow_color=(235, 220, 130), line_color=(225, 200, 120))
btn_reg = Button(all_sprites, register, (170, 10, 150, 25), 'Зарегистрироваться', body_color=(255, 240, 150),
                 shadow_color=(235, 220, 130), line_color=(225, 200, 120))

btn_fool = Button(all_sprites, fool, (10, 180, 200, 25), 'Дурак', body_color=(170, 220, 255),
                  shadow_color=(150, 200, 235), line_color=(130, 170, 215))
btn_gallows = Button(all_sprites, gallows, (10, 220, 200, 25), 'Виселица', body_color=(170, 220, 255),
                     shadow_color=(150, 200, 235), line_color=(130, 170, 215))
btn_solitare = Button(all_sprites, solitaire, (10, 260, 200, 25), 'Косынка', body_color=(170, 220, 255),
                      shadow_color=(150, 200, 235), line_color=(130, 170, 215))

label_1 = Label(all_sprites, 'Тут будет инфа о пользователе', (10, 50), 30, 50)
label = Label(all_sprites, 'Каталог игр', (10, 150), 25, 50)

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
