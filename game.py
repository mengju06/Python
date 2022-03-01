import pygame
import random
import os
import time


FPS = 60
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
HEIGHT = 900
WIDTH = 1600
# k = 0
running = True
score = 0
health = 100

#遊戲初始化 創建視窗
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("有勝尬夢幻")
clock = pygame.time.Clock()

#圖片
player_img = pygame.image.load(os.path.join("img", "player.png")).convert()
player_img.set_colorkey(BLACK)
pygame.display.set_icon(player_img)
background_img = pygame.image.load(os.path.join("img", "background.jpg")).convert()
background_img = pygame.transform.scale(background_img,(1600, 900))
gas_img = pygame.image.load(os.path.join("img", "gas.png")).convert()
house_img = pygame.image.load(os.path.join("img", "house.png")).convert()
house_img.set_colorkey(BLACK)
house_img = pygame.transform.scale(house_img,(300, 674))
people_imgs = []
for i in range(8):
    people_imgs.append(pygame.image.load(os.path.join("img", f"people{i}.png")).convert())
dream_imgs = []
for i in range(5):
    dream_imgs.append(pygame.image.load(os.path.join("img", f"dream{i}.png")).convert())

#文字
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LEANGTH = 200
    BAR_HEIGHT = 20
    fill = (hp/100)*BAR_LEANGTH
    outline_rect = pygame.Rect(x, y, BAR_LEANGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

#音樂
# background_sound = pygame.mixer.Sound(os.path.join("sound", "background.wav"))
pygame.mixer.music.load(os.path.join("sound", "background.wav"))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (240,156))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT)
        self.speedx = 5
        self.speedy = 8

    def update(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speedy
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        gas = Gas(self.rect.right, self.rect.centery + 15)
        all_sprites.add(gas)
        Gases.add(gas)

class People(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(random.choice(people_imgs), (102,153))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH, 1000 + WIDTH)
        self.rect.y = random.randrange(150,HEIGHT-156) 
        self.speedx = random.randrange(-5,-2)
        self.mask = pygame.mask.from_surface(self.image)
               
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:            
            self.image = pygame.transform.scale(random.choice(people_imgs), (102,153))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH, 1000 + WIDTH)
            self.rect.y = random.randrange(150,HEIGHT-156)
            self.speedx = random.randrange(-5,-2)          

class Dream(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(random.choice(dream_imgs), (102,153))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH, 1000 + WIDTH)
        self.rect.y = random.randrange(150,HEIGHT-156) 
        self.speedx = random.randrange(-5,-2)
        self.mask = pygame.mask.from_surface(self.image)
               
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:            
            self.image = pygame.transform.scale(random.choice(dream_imgs), (102,153))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH, 1000 + WIDTH)
            self.rect.y = random.randrange(150,HEIGHT-156)
            self.speedx = random.randrange(-5,-2)

class Gas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = pygame.transform.scale(gas_img, (15,35))        
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y 
        self.speedx = 10
        self.mask = pygame.mask.from_surface(self.image)       
        self.rot_degree = -2    
        self.total_degree = 0 

    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center


    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
Peoples = pygame.sprite.Group()
Dreams = pygame.sprite.Group()
Gases = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
for i in range(8):
    people = People()
    all_sprites.add(people)
    Peoples.add(people)

for i in range(3):
    dream = Dream()
    all_sprites.add(dream)
    Dreams.add(dream)



#音樂
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.01)

#遊戲迴圈
while running:
    clock.tick(FPS)
    #輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    #更新
    all_sprites.update()
    hits = pygame.sprite.groupcollide(Peoples, Gases, True, True, pygame.sprite.collide_mask)
    for hit in hits:
        people = People()
        all_sprites.add(people)
        Peoples.add(people)
        score += 100

    mistakes = pygame.sprite.groupcollide(Dreams, Gases, True, True, pygame.sprite.collide_mask)
    for mistake in mistakes:
        dream = Dream()
        all_sprites.add(dream)
        Dreams.add(dream)
        score -= 100

    if score < 0:
        score = 0

    for people in Peoples:
        if people.rect.right < 0:
            health -= 10

    #輸出
    screen.fill(BLACK)
    screen.blit(background_img, (0,0))
    screen.blit(house_img, (0,200))
    # screen.blit(background_img, (WIDTH + k,0))
    # k -= 10
    # if k == -WIDTH:
    #     screen.blit(background_img, (WIDTH + k,0))
    #     k = 0
    all_sprites.draw(screen)
    draw_text(screen, 'SCORE:', 30, 80, 30)
    draw_text(screen, str(score), 30, 180, 30)
    draw_health(screen, health, 70, 90)
    draw_text(screen, str(health), 25, 180, 85)
    pygame.display.update()

pygame.quit()