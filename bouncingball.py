import pygame
import os
os.system("cls")

class Ball():
    def __init__(self,radius,x_init,y_init,x_speed,y_speed,clr,screen) -> None:
        self.radius = radius
        self.x = x_init
        self.y = y_init
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.clr = clr
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > self.width-self.radius or self.x < self.radius:
            self.x_speed *= -1
        if self.y > self.height-self.radius or self.y < self.radius:
            self.y_speed *= -1

    def draw(self):
        pygame.draw.circle(self.screen,self.clr,(self.x, self.y),self.radius)


width = 800
height = 600
screen_size = (width,height)

pygame.init()
win = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Bouncing Ball Program by Anakan Gopalan")

balls = []

balls.append(Ball(20,100,100,3,3,"red",win))
balls.append(Ball(40,45,60,2,4,"green",win))

fps = 60
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill("cyan")

    
    for ball in balls:
        ball.update()
        ball.draw()

    pygame.display.flip()

pygame.quit()