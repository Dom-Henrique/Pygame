import pygame as pg

pg.init()

largura = 600
altura = 600
tela = pg.display.set_mode((altura, largura))
pg.display.set_caption('Olá, mundo!')

rodar = True
while rodar:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rodar = False
            
pg.quit()