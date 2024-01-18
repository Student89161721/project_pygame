from PyQt5.QtWidgets import QApplication

from reg_login import nickname_, score_, register, login
from fooldir.fool import fool_run, end_display
from gallowsdir.gallows import gallows_run
from soldir.solitaire import SolitaireMenu, solitaire_run
from PGWigets import *
import sqlite3
import pygame
global nickname_, score_


WIDTH, HEIGHT = 400, 400

all_sprites = pygame.sprite.Group()


def log():
    global nickname_
    global score_
    nickname_, score_ = login()


def reg():
    global nickname_
    global score_
    nickname_, score_ = register()


def solitaire_menu():
    app = QApplication(sys.argv)
    solitaire_menu = SolitaireMenu()
    solitaire_menu.show()
    app.exec()


def fool():
    global screen
    winner = fool_run(screen)
    if not winner is None:
        if not end_display(winner, screen) is None:
            fool()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


def gallows():
    global screen
    winner = gallows_run(screen)
    if not winner is None:
        if not end_display(winner, screen) is None:
            gallows()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


def solitaire():
    global screen
    solitaire_menu()
    winner = solitaire_run(screen)
    if not winner is None:
        if not end_display(winner, screen) is None:
            solitaire()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

btn_log = Button(all_sprites, log, (10, 10, 150, 25), 'Войти', body_color=(255, 240, 150),
                 shadow_color=(235, 220, 130), line_color=(225, 200, 120))
btn_reg = Button(all_sprites, reg, (170, 10, 150, 25), 'Зарегистрироваться', body_color=(255, 240, 150),
                 shadow_color=(235, 220, 130), line_color=(225, 200, 120))

btn_fool = Button(all_sprites, fool, (10, 180, 200, 25), 'Дурак', body_color=(170, 220, 255),
                  shadow_color=(150, 200, 235), line_color=(130, 170, 215))
btn_gallows = Button(all_sprites, gallows, (10, 220, 200, 25), 'Виселица', body_color=(170, 220, 255),
                     shadow_color=(150, 200, 235), line_color=(130, 170, 215))
btn_solitare = Button(all_sprites, solitaire, (10, 260, 200, 25), 'Косынка', body_color=(170, 220, 255),
                      shadow_color=(150, 200, 235), line_color=(130, 170, 215))
label = Label(all_sprites, 'Каталог игр', (10, 150), 25, 50)

con = sqlite3.connect("gallowsdir/database.db")
cur = con.cursor()
label_1 = Label(all_sprites, f'Имя пользователя: {nickname_}', (10, 50), 30, 50)
label_2 = Label(all_sprites, f'Ваши очки: {score_}', (10, 70), 30, 50)
con.close()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)
    if label_1.text != f'Имя пользователя: {nickname_}':
        label_1.set_text(f'Имя пользователя: {nickname_}')
    if label_2.text != f'Ваши очки: {score_}':
        label_2.set_text(f'Ваши очки: {score_}')
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

