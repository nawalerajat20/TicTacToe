import pygame as pg
import pygame_menu
import sys
import time
from pygame.locals import *

winner = None
draw = None
XO = 'x'
width = 600
height = 600
board = [[None]*3, [None]*3, [None]*3]
white = (255, 255, 255)
line_color = (0, 0, 0)

pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)

pg.display.set_caption("Tic Tac Toe")
initiating_window = pg.image.load("3-3 grid.jpg")
x_img = pg.image.load("X-img.png")
y_img = pg.image.load("o.png")

initiating_window = pg.transform.scale(
    initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (150, 150))
o_img = pg.transform.scale(y_img, (150, 150))


def game_initiating_window():

    screen.blit(initiating_window, (0, 0))
    pg.display.update()
    time.sleep(3)
    screen.fill(white)
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0),
                   (width / 3 * 2, height), 7)
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2),
                   (width, height / 3 * 2), 7)
    draw_status()


def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = "Game Draw !"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 600, 700, 100))
    text_rect = text.get_rect(center=(width / 2, 700-50))
    screen.blit(text, text_rect)
    pg.display.update()


def check_win():
    global board, winner, draw

    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0),
                           (0, (row + 1)*height / 3 - height / 6),
                           (width, (row + 1)*height / 3 - height / 6),
                           4)
            break

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
                           ((col + 1) * width / 3 - width / 6, height), 4)
            break

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):

        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (0, 0), (600, 600), 4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (600, 0), (0, 600), 4)

    if(all([all(row) for row in board]) and winner is None):
        draw = True
    draw_status()


def drawXO(row, col):
    global board, XO
    if row == 1:
        posx = 55

    if row == 2:
        posx = width / 3 + 55

    if row == 3:
        posx = width / 3 * 2 + 55

    if col == 1:
        posy = 55

    if col == 2:
        posy = height / 3 + 55

    if col == 3:
        posy = height / 3 * 2 + 55

    board[row-1][col-1] = XO

    if(XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'

    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()


def user_click():

    x, y = pg.mouse.get_pos()

    if(x < width / 3):
        col = 1

    elif (x < width / 3 * 2):
        col = 2

    elif(x < width):
        col = 3

    else:
        col = None

    if(y < height / 3):
        row = 1

    elif (y < height / 3 * 2):
        row = 2

    elif(y < height):
        row = 3

    else:
        row = None

    if(row and col and board[row-1][col-1] is None):
        global XO
        drawXO(row, col)
        check_win()


def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window()
    menu.mainloop(screen)
    winner = None
    board = [[None]*3, [None]*3, [None]*3]


def start1():
    game_initiating_window()


    while(True):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                user_click()
            if(winner or draw):
                reset_game()
        pg.display.update()
        CLOCK.tick(fps)

winner2 = None
draw2 = None
XO = 'x'
width2 = 600
height2 = 600
board2 = [[None]*4, [None]*4, [None]*4, [None]*4]
white2 = (255, 255, 255)
line_color2 = (0, 0, 0)

pg.init()
fps2 = 30
CLOCK = pg.time.Clock()
screen2 = pg.display.set_mode((width2, height2+100), 0, 32)

pg.display.set_caption("Tic Tac Toe")
initiating_window2 = pg.image.load("tictactoedeluxe480.png")
x_img = pg.image.load("X-img.png")
y_img = pg.image.load("o.png")

initiating_window2 = pg.transform.scale(
    initiating_window2, (width2, height2 + 100))
x_img = pg.transform.scale(x_img, (90, 90))
o_img = pg.transform.scale(y_img, (90, 90))


def game_initiating_window2():

    screen2.blit(initiating_window2, (0, 0))
    pg.display.update()
    time.sleep(3)
    screen2.fill(white2)
    pg.draw.line(screen2, line_color2, (width2 / 4, 0),
                   (width2 / 4, height2), 7)
    pg.draw.line(screen2, line_color2, (width2 / 4 * 2, 0),
                   (width2 / 4 * 2, height2), 7)
    pg.draw.line(screen2, line_color2, (width2 / 4 * 3, 0),
                   (width2 / 4 * 3, height2), 7)
    pg.draw.line(screen2, line_color2, (0, height2 / 4),
                   (width2, height2 / 4), 7)

    pg.draw.line(screen2, line_color2, (0, height2 / 4 * 2),
                   (width2, height2 / 4 * 2), 7)
    pg.draw.line(screen2, line_color2, (0, height2 / 4 * 3),
                   (width2, height2 / 4 * 3), 7)
    draw_status2()


def draw_status2():
    global draw2

    if winner2 is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner2.upper() + " won !"
    if draw:
        message = "Game Draw !"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen2.fill((0, 0, 0), (0, 600, 700, 100))
    text_rect = text.get_rect(center=(width2 / 2, 700-50))
    screen2.blit(text, text_rect)
    pg.display.update()


def check_win2():
    global board2, winner2, draw2

    for row in range(0, 4):
        if((board2[row][0] == board2[row][1] == board2[row][2] == board2[row][3]) and (board2[row][0] is not None)):
            winner2 = board2[row][0]
            pg.draw.line(screen2, (250, 0, 0),
                           (0, (row + 1)*height2 / 4 - height2 / 8),
                           (width2, (row + 1)*height2 / 4 - height2 / 8),
                           4)
            break

    for col in range(0, 4):
        if((board2[0][col] == board2[1][col] == board2[2][col] == board2[3][col]) and (board2[0][col] is not None)):
            winner2 = board2[0][col]
            pg.draw.line(screen2, (250, 0, 0), ((col + 1) * width2 / 4 - width2 / 8, 0),
                           ((col + 1) * width2 / 4 - width2 / 8, height2), 4)
            break

    if (board2[0][0] == board2[1][1] == board2[2][2] == board2[3][3]) and (board2[0][0] is not None):

        winner2 = board2[0][0]
        pg.draw.line(screen2, (250, 70, 70), (0, 0), (600, 600), 4)

    if (board2[0][3] == board2[1][2] == board2[2][1] == board2[3][0]) and (board2[0][3] is not None):
        winner2 = board2[0][3]
        pg.draw.line(screen2, (250, 70, 70), (600, 0), (0, 600), 4)

    if(all([all(row) for row in board2]) and winner2 is None):
        draw2 = True
    draw_status2()


def drawXO2(row, col):
    global board2, XO
    if row == 1:
        posx = 30

    if row == 2:
        posx = width2 / 4 + 30

    if row == 3:
        posx = width2 / 4 * 2 + 30

    if row == 4:
        posx = width2 / 4 * 3 + 30

    if col == 1:
        posy = 30

    if col == 2:
        posy = height2 / 4 + 30

    if col == 3:
        posy = height2 / 4 * 2 + 30

    if col == 4:
        posy = height2 / 4 * 3 + 30

    board2[row-1][col-1] = XO

    if(XO == 'x'):
        screen2.blit(x_img, (posy, posx))
        XO = 'o'

    else:
        screen2.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()


def user_click2():

    x, y = pg.mouse.get_pos()

    if(x < width2 / 4):
        col = 1
    elif (x < width2 / 4 * 2):
        col = 2
    elif (x < width2 / 4 * 3):
        col = 3
    elif(x < width2):
        col = 4

    else:
        col = None

    if(y < height2 / 4):
        row = 1
    elif (y < height2 / 4 * 2):
        row = 2
    elif (y < height2 / 4 * 3):
        row = 3
    elif(y < height2):
        row = 4

    else:
        row = None

    if(row and col and board2[row-1][col-1] is None):
        global XO
        drawXO2(row, col)
        check_win2()


def reset_game2():
    global board2, winner2, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window2()
    menu.mainloop(screen)
    winner2 = None
    board2 = [[None]*4, [None]*4, [None]*4, [None]*4]


def start2():
    game_initiating_window2()
    while(True):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                user_click2()
            if(winner2 or draw):
                reset_game2()
        pg.display.update()
        CLOCK.tick(fps2)


menu = pygame_menu.Menu('TIC-TAC-TOE', 570, 670,
                        theme=pygame_menu.themes.THEME_DARK)

image_path = pygame_menu.baseimage.IMAGE_EXAMPLE_PYGAME_MENU
menu.add.image(image_path, angle=0, scale=(0.15, 0.15))

menu.add.text_input('Enter Name of Player 1 :', default=' ')
menu.add.text_input('Enter Name of Player 2 :', default=' ')
menu.add.button('3 x 3', start1)
menu.add.button('4 x 4', start2)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

