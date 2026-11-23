
import pygame

print("PROGRAM STARTED", flush=True)

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("My First Weather App")

print("WINDOW CREATED", flush=True)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 180, 255))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
