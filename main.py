import pygame
import math
from kinematics import inverse_kinematics

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

origin = (400, 300)
l1, l2 = 150, 100

running = True
target = origin

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target = pygame.mouse.get_pos()

    theta1, theta2 = inverse_kinematics(origin, target, l1, l2)

    x1 = origin[0] + l1 * math.cos(theta1)
    y1 = origin[1] + l1 * math.sin(theta1)

    x2 = x1 + l2 * math.cos(theta1 + theta2)
    y2 = y1 + l2 * math.sin(theta1 + theta2)

    pygame.draw.line(screen, (0,0,0), origin, (x1, y1), 5)
    pygame.draw.line(screen, (0,0,255), (x1, y1), (x2, y2), 5)

    pygame.display.flip()

pygame.quit()
