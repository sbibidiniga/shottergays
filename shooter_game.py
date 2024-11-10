from pygame import *
import pygame
import random
def game():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('space.ogg')
    pygame.mixer.music.play()

    windows = pygame.display.set_mode((700,500))



    FPS = pygame.time.Clock()

    fon = pygame.image.load('galaxy.jpg')
    fon = pygame.transform.scale(fon,(700,500))
    class   GameObject(pygame.sprite.Sprite):
        def __init__(self,image,visota,shirina,x,y,speed):
            super().__init__()
            self.img_sprite = pygame.image.load(image)
            self.img_sprite = pygame.transform.scale(self.img_sprite,(visota,shirina))
            self.rect = self.img_sprite.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.speed = speed
            self.move =''
        def show(self):
            windows.blit(self.img_sprite,self.rect)


    class   gamePlayer(GameObject):
        def ypravlenie(self):
            keys = pygame.key.get_pressed()


            if keys[pygame.K_d] and self.rect.x < 650:
                self.rect.x += self.speed
            if keys[pygame.K_a] and self.rect.x > 0 :
                self.rect.x -= self.speed
        def vistrel(self):
            puly = Puly('bullet.png',15,20,self.rect.x,self.rect.y,10)
            pulys.add(puly)

    class Enemy(GameObject):
        def forward(self):
            self.rect.y += 2
            if self.rect.y > 400:
                self.rect.y = -20
                self.rect.x = random.randint(50,650)


    class Puly(GameObject):
        def update(self):
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()


    pulys = sprite.Group()




    player = gamePlayer('rocket.png',60,60,20,420,3)

    money = GameObject('bullet.png',60,60,400,90,0)


    run = True
    monstrers = pygame.sprite.Group()
    for i in range(5):
        monster = Enemy('ufo.png',60,60,random.randint(80,1120),-100,1)
        monstrers.add(monster)
        
    score = 0

    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

            elif i.type == KEYDOWN:
                if i.key == K_SPACE:
                    player.vistrel()
        kill = pygame.sprite.groupcollide(pulys,monstrers,True,True)
        for i in kill:
            score +=1
            monster = Enemy('ufo.png',60,60,random.randint(80,1120),-100,1)
            monstrers.add(monster)
        
        windows.blit(fon,(0,0))
        player.show()
        player.ypravlenie()
        for i in pulys:
            i.show()
            i.update()
        for i in monstrers:
            i.show()
            i.forward()
            if player.rect.colliderect(i.rect):
                run = False
        pygame.display.update()
        FPS.tick(100)