import pygame

class charas():
    def __init__(self):
        self.position = [50,210]
        self.img = [
                    pygame.image.load("./image/01.png"),
                    pygame.image.load("./image/02.png"),
                    pygame.image.load("./image/03.png"),
                    pygame.image.load("./image/04.png")
                ]
        self.speed = 10 
        self.dirX = "right" 
        self.dirY = "None" 
    
    def run(self,keys):
        if keys[pygame.K_UP]:
            if self.dirY =="None":
                self.dirY = "up"
        if keys[pygame.K_LEFT]:
            if self.position[0] > 10:
                self.position[0] -= self.speed
                self.dirX = "left"
        if keys[pygame.K_RIGHT]:
            if self.position[0] <= 550:
                self.position[0] += self.speed
                self.dirX = "right"
                
    def jumping(self):
        #視高度調整速度
        if self.position[1] < 140:
            self.dirY = "down"
        if self.dirY == "down":
            if self.position[1] >= 210:
                self.dirY = "None"
        if self.dirY == "up":
            self.position[1] -= self.speed * (1 + self.position[1] // 1000)
        elif self.dirY == "down":
            self.position[1] += self.speed * (1 + self.position[1] // 1000)