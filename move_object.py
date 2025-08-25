import pygame as pg

pg.init()
# Configurações de tela
largura = 600
altura = 600
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Moving objects')

# Atributos do objeto
x = 10
y = 10
largura_pixel = 40
altura_pixel = 50
velocidade = 0.1

# Rodar aplicação
rodar = True

while rodar:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rodar = False
    # Movendo os objetos
    teclas = pg.key.get_pressed() # Lista de teclas
    
    if teclas[pg.K_LEFT] or teclas[pg.K_a]:
        x -= velocidade
    elif teclas[pg.K_RIGHT] or teclas[pg.K_d]:
        x += velocidade
    elif teclas[pg.K_UP] or teclas[pg.K_w]:
        y -= velocidade
    elif teclas[pg.K_DOWN] or teclas[pg.K_s]:
        y += velocidade
    # Desenhando os objetos
    tela.fill((0, 0, 0))
    pg.draw.rect(tela, (255, 255, 255), (x, y, largura_pixel, altura_pixel), 0, 10)
    pg.display.update()
            
pg.quit()