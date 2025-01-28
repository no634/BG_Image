import pygame

pygame.init()

width, height = 800, 600
FPS = 60
img1 = 'Tennis_court.jpg'  # Replace with your actual image path
img2 = 'picture.jpg'  # Replace with your actual image path

# Load the images
background1 = pygame.image.load(img1)
background2 = pygame.image.load(img2)

background1 = pygame.transform.scale(background1, (width,height))
background2 = pygame.transform.scale(background2, (width,height))
f = background1  # Start with the first background

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Switch the background when spacebar is pressed
                f = background2 if f == background1 else background1

    # Draw the current background
    screen.blit(f, (0, 0))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()