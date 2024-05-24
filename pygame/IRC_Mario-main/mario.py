import pygame

pygame.init()
pygame.display.set_caption("Mario")
screen = pygame.display.set_mode((640,360))

background = pygame.image.load("/Users/liyingxuan/Desktop/coding/IRC2024/pygame/IRC_Mario-main/image/background.png")
running = True

def isbricksrun(brick,keys,chara_position):
        if brick.position[0] >= 640 -brick.img.get_size()[0]:
            if keys[pygame.K_RIGHT]:
                if chara_position>500:
                    return True
        return False

class bricks():
    def __init__(self,i):
        self.img = pygame.image.load("/Users/liyingxuan/Desktop/coding/IRC2024/pygame/IRC_Mario-main/image/brick.png")
        self.position = [self.img.get_size()[0]*i,305]
        self.show = True
    def run(self,speed):
        self.position[0]-=speed
    def drop(self,chara):
        if self.ischaradrop(chara):
            chara.life = False
    def ischaradrop(self,chara):
        if not self.show:
            if chara.position[1]>=210:
                    if abs(chara.position[0] + chara.img.get_size()[0] - self.position[0] - self.img.get_size()[0]) < 5:   
                        return True
        return False

    




brick = []
for i in range(24):
        brick .append(bricks(i))
class charas():
     def  __init__(self):
        self.img = pygame.image.load("/Users/liyingxuan/Desktop/coding/IRC2024/pygame/IRC_Mario-main/image/01.png")
        self.position = [50,210]
        self.speed = 10
        self.dirY = "None" 
        self.life= True
     def run(self,keys):
        if keys[pygame.K_UP]:
         if self.dirY =="None":
                self.dirY = "up"
        if keys[pygame.K_LEFT]:
             if self.position[0]>10:
                self.position[0]-=self.speed
                self.dirX = "left"
                
        if keys[pygame.K_RIGHT]:
             if self.position[0]<=500:
                self.position[0]+=self.speed
                self.dirX = "right"  
     def jumping(self):
        if self.position[1] < 140:
            self.dirY = "down"
        if self.dirY == "down":
            if self.position[1] >= 210:
                self.dirY = "None"
        if self.dirY == "up":
            self.position[1] -= self.speed * (1 + self.position[1] // 1000)
        elif self.dirY == "down":
            self.position[1] += self.speed * (1 + self.position[1] // 1000)
     def down(self):
         if not self.life :
             self.jump=False
             if self.position[1] < 460:
                 self.position[1]+= self .speed
                 return True
             else:
                 return False
         return True
class golds():
    def __init__(self) :
        self.position =[355,250]
        self.img = [pygame.image.load("/Users/liyingxuan/Desktop/coding/IRC2024/pygame/IRC_Mario-main/image/ggl.png")]
        self.show = True
    def eat(self,chara_position):
        if abs(chara_position[0] - self.position[0]<20) and abs(chara_position[1] - self.position[1]<50):
            self.show = False
    def run(self):
        self.position[0]-=10
    def setPosition(self,i):
        self.show = True
        if i < 5:
            if i == 2:
                self.position = [200+50*i,160]
            else:
                self.position = [200+50*i,250]
        else:
            if i==7:
                self.position = [500+50*i,160]
            else:
                self.position = [500+50*i,250]


                          
chara = charas()

brick[5].show =False
brick[10].show =False 
brick[15].show =False

while running:
    keys = pygame.key.get_pressed()
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if isbricksrun(brick[23],keys,chara.position[0]):
         for i in range(24):
             brick[i].run(chara.speed)
         for i in range(10):
             gold[i].run()
             
    else :
            chara.run(keys)
    for i in range(24):
        brick[i].drop(chara)

    running= chara.down()

    for i in range(5):
        screen.blit(background,[i*160,0])



    for i in range (24):
        if brick[i].show:
            screen.blit(brick[i].img,brick[i].position)
    gold= []
    for i in range(10):
        gold.append(gold,golds())
        gold[i].setPosition(i)
    for i in range(10):
        if gold[i].show:
            gold[i].eat(chara.position)
            screen.blit(gold[i].img,gold[i].position)
    

    
    chara.jumping()    
    chara.run(keys)
    screen.blit(chara.img,chara.position)
    clock = pygame.time.Clock()
    clock.tick(35)






    pygame.display.update()
