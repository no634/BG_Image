import pygame

pygame.init()

width = 800
height = 600
FPS = 60
img1 = 'Tennis_court.jpg'
img2 = 'picture.jpg'

img2 = pygame.image.load(img2)
img1 = pygame.image.load(img1)

img1 = pygame.transform.scale(img1, (width,height))
img2 = pygame.transform.scale(img2, (width,height))
f = img1

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                f = img2 if f == img1 else img1

    screen.blit(f, (0, 0))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()