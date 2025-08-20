import pygame as pg

pg.init()

screen = pg.display.set_mode((400,400)) # Define o tamanho da tela
pg.display.set_caption('Meu primeiro jogo')
pg.display.set_palette(('hhhhh'))

running = True
while running:
    for event in pg.event.get(): # Evento pego
        if event.type == pg.QUIT:
            running = False
            
pg.quit()