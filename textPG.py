import pygame as pg

pg.init()
pg.font.init()

tela = pg.display.set_mode((600, 600)) # Define o tamanho da tela
pg.display.set_caption('Olá! Esse é o meu primeiro jogo!') # Define o título da janela
azul = (0, 0, 255)

# Define as configurações
fonte = pg.font.SysFont(None, 48)
text = fonte.render('Olá, mundo!', True, (255, 255, 255))
centerText = text.get_rect()
# centerText.center = 

rodar = True

while rodar:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rodar = False
    tela.fill(azul)
    
    tela.blit(text, centerText)
    pg.display.update()
      
pg.quit()