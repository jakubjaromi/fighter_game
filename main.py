from sys import exit
import pygame
import random


pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fighter')
clock = pygame.time.Clock()
scale = 0.8
moving_left = False
moving_right = False
life_status = 5


class Background(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('graphics/bg.jpg').convert()
        self.image = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self):
        screen.blit(self.image, (0, 0))


class Heart(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)

        img_1 = pygame.image.load('graphics/heart_1.png').convert_alpha()
        # img_1 = pygame.transform.scale(img_1,
        #                                (int(img_1.get_width() * scale * 1.2), int(img_1.get_height() * scale * 1.2)))

        img_2 = pygame.image.load('graphics/heart_2.png').convert_alpha()
        # img_2 = pygame.transform.scale(img_2,
        #                                (int(img_2.get_width() * scale * 1.2), int(img_2.get_height() * scale * 1.2)))
        self.image_list = [img_1, img_2]

    def draw(self, life_status):
        current_life_status = life_status
        positions = [(10, 10), (70, 10), (130, 10), (190, 10), (250, 10)]
        for position in positions:
            if current_life_status == 0:
                screen.blit(self.image_list[1], position)
            else:
                screen.blit(self.image_list[0], position)

            current_life_status += -1
            if current_life_status < 0:
                current_life_status = 0



class Boss(pygame.sprite.Sprite):

    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('graphics/boss.png').convert_alpha()
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()

    def positioning(self, x, y):
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):

    def __init__(self, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.image_index = 0
        self.gravity = 0

        img_1 = pygame.image.load('graphics/player_1.png').convert_alpha()
        img_1 = pygame.transform.scale(img_1,
                                       (int(img_1.get_width() * scale * 1.2), int(img_1.get_height() * scale * 1.2)))

        img_2 = pygame.image.load('graphics/player_2.png').convert_alpha()
        img_2 = pygame.transform.scale(img_2,
                                       (int(img_2.get_width() * scale * 1.2), int(img_2.get_height() * scale * 1.2)))
        self.image_list = [img_1, img_2]
        self.image = self.image_list[self.image_index]
        self.rect = self.image.get_rect()

    def positioning(self, x, y):
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        self.rect.x += dx
        self.rect.y += dy

        if moving_left or moving_right:
            self.image_index += 0.12
            if self.image_index >= len(self.image_list):
                self.image_index = 0
            self.image = self.image_list[int(self.image_index)]
        else:
            self.image = self.image_list[0]

    def jump(self):
        self.image = self.image_list[0]
        self.gravity = -15

    def draw(self):
        self.gravity += 1
        self.rect.y += self.gravity

        # limit for bottom value
        if self.rect.bottom >= int(SCREEN_HEIGHT - self.image.get_height()):
            self.rect.bottom = int(SCREEN_HEIGHT - self.image.get_height())

        # limit for top value
        if self.rect.top < 0:
            self.rect.top = 0

        # limit for left value
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > int(SCREEN_WIDTH / 2):
            self.rect.right = int(SCREEN_WIDTH / 2)

        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


# create background
bg = Background()

hp = Heart(scale)

# create boss
boss = Boss(scale)
boss.positioning(int(SCREEN_WIDTH - (boss.image.get_width()/2)), int(SCREEN_HEIGHT - (boss.image.get_height()/2)) - 95)

# create player
player = Player(scale, 4)
player.positioning(int(player.image.get_width()/2) + 100, int(SCREEN_HEIGHT - player.image.get_height()) - 45)

run = True
while run:

    # draw background
    bg.draw()

    # draw hp hearts
    hp.draw(life_status)

    # draw boss
    boss.draw()

    # draw player
    player.draw()
    player.move(moving_left, moving_right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    # update everything
    pygame.display.update()
    clock.tick(60)


