import pygame
import sys

pygame.init() # inicia o py game

#pygame.mixer.init()

windowSize = (1000, 800) # tamanho da janela passado como tupla, pois não via mudar

screen = pygame.display.set_mode(windowSize) # instancia na variável screen, o tamanho da janela

helloWorld = pygame.image.load("ship.png") # atribui a variável uma imagem
bg = pygame.image.load("bg.jpeg") # atribui a variável uma imagem

pygame.mouse.set_visible(0)

helloWorldSize = helloWorld.get_size()

x, y = 0, 0
clock = pygame.time.Clock()


while 1:

    clock.tick(100)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        """if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                x += 50 #if x >= 0 else 0
            if events.key == pygame.K_LEFT:
                x -= 50 #if x >= 0 else 0

            if events.key == pygame.K_UP:
                y -= 50 #if y >= 0 else 0
            if events.key == pygame.K_DOWN:
                y += 50 #if y >= 0 else 0"""



    screen.fill((255, 255, 255))

    mousePosition = pygame.mouse.get_pos()

    x, y = mousePosition

    print(x, y)

    if x + helloWorldSize[0] > 1000:
        x = 1000 - helloWorldSize[0]

    if y + helloWorldSize[1] > 800:
        y = 800 - helloWorldSize[1]

    screen.blit(bg, (0, 0))
    screen.blit(helloWorld, (x, y))


    pygame.display.update()