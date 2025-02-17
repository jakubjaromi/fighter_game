from sys import exit
import pygame
import random


pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fighter')
clock = pygame.time.Clock()
boss_font = pygame.font.Font('font/Minecraft.ttf', 36)
menu_font = pygame.font.Font('font/Minecraft.ttf', 50)
scale = 0.8
moving_left = False
moving_right = False
moving_attack = False
life_status = 5
game_init = True
easy_arrow = ' <'
medium_arrow = ''
hard_arrow = ''
max_fireballs = 3

class Background(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('graphics/bg.jpg').convert()
        self.image = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self):
        screen.blit(self.image, (0, 0))


class Heart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        img_1 = pygame.image.load('graphics/heart_1.png').convert_alpha()
        img_1 = pygame.transform.scale(img_1,
                                       (int(img_1.get_width() * scale), int(img_1.get_height() * scale)))

        img_2 = pygame.image.load('graphics/heart_2.png').convert_alpha()
        img_2 = pygame.transform.scale(img_2,
                                       (int(img_2.get_width() * scale), int(img_2.get_height() * scale)))
        self.image_list = [img_1, img_2]

    def draw(self):
        current_life_status = life_status
        positions = [(10, 10), (60, 10), (110, 10), (160, 10), (210, 10)]
        for position in positions:
            if current_life_status == 0:
                screen.blit(self.image_list[1], position)
            else:
                screen.blit(self.image_list[0], position)

            current_life_status += -1
            if current_life_status < 0:
                current_life_status = 0


class Boss(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cool_down_count = 0
        self.image_index = 0
        self.image_fireball_index = 0
        self.current_hp = 10000
        self.fireball_list = list()

        # img = pygame.image.load('graphics/boss_3.png').convert_alpha()
        # # self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        # self.image = pygame.transform.scale(img, (int(img.get_width() * 1.1), int(img.get_height() * 1.1)))
        # self.rect = self.image.get_rect()

        #
        img_1 = pygame.image.load('graphics/boss_1.png').convert_alpha()
        img_1 = pygame.transform.scale(img_1, (int(img_1.get_width() * 0.9), int(img_1.get_height() * 0.9)))

        img_2 = pygame.image.load('graphics/boss_2.png').convert_alpha()
        img_2 = pygame.transform.scale(img_2, (int(img_2.get_width() * 0.9), int(img_2.get_height() * 0.9)))

        img_3 = pygame.image.load('graphics/boss_3.png').convert_alpha()
        img_3 = pygame.transform.scale(img_3, (int(img_3.get_width() * 0.9), int(img_3.get_height() * 0.9)))
        self.image_list = [img_1, img_2, img_3]
        self.image = self.image_list[self.image_index]
        self.rect = self.image.get_rect()

        img_fireball_1 = pygame.image.load('graphics/fileball_1.png').convert_alpha()
        img_fireball_2 = pygame.image.load('graphics/fileball_2.png').convert_alpha()
        self.image_fireball_list = [img_fireball_1, img_fireball_2]
        self.image_fireball = self.image_fireball_list[self.image_fireball_index]
        self.rect_fireball = self.image_fireball.get_rect()

    def positioning(self, x, y):
        self.rect.center = (x, y)

    def draw(self):
        # draw boss
        self.image_index += 0.03
        if self.image_index >= len(self.image_list):
            self.image_index = 0
        self.image = self.image_list[int(self.image_index)]
        screen.blit(self.image, self.rect)

        # draw boss's hp
        text_hp = boss_font.render(f'Boss HP: {self.current_hp}/10000', False, 'White').convert()
        screen.blit(text_hp, (SCREEN_WIDTH - 400, 25))

        # draw boss's fireballs
        self.cooldown()
        if self.cool_down_count == 0:
            self.cool_down_count = 1
            if len(self.fireball_list) < max_fireballs:
                if max_fireballs == 3:
                    fireballs_speed = random.randint(2, 5)
                elif max_fireballs == 4:
                    fireballs_speed = random.randint(3, 7)
                else:
                    fireballs_speed = random.randint(4, 10)
                self.rect_fireball.x = self.rect.x - random.randint(20, 40)
                self.rect_fireball.y = self.rect.y - random.randint(100, 300)
                self.fireball_list.append([self.rect.x - random.randint(20, 40),
                                           self.rect.y + random.randint(0, 450),
                                           fireballs_speed,
                                           0])

        temp_fireball_list = list()
        if self.fireball_list:
            temp_fireball_list.clear()
            for fireball in self.fireball_list:
                current_fireball_x = fireball[0]
                current_fireball_y = fireball[1]
                current_fireball_speed = fireball[2]
                current_fireball_index = fireball[3]
                current_fireball_index += 0.2
                if current_fireball_index >= len(self.image_fireball_list):
                    current_fireball_index = 0
                image_fireball = self.image_fireball_list[int(current_fireball_index)]

                rect_fireball = image_fireball.get_rect()
                rect_fireball.x = current_fireball_x - current_fireball_speed
                current_fireball_x = current_fireball_x - current_fireball_speed
                rect_fireball.y = current_fireball_y
                screen.blit(image_fireball, rect_fireball)

                if rect_fireball.x > 0:
                    temp_fireball_list.append([current_fireball_x, current_fireball_y,
                                               current_fireball_speed, current_fireball_index])

            self.fireball_list = temp_fireball_list.copy()

    def cooldown(self):
        if self.cool_down_count >= 20:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def check_fireball_hit(self, rect_hero):
        global life_status
        temp_fireball_list = list()
        if self.fireball_list:
            for fireball in self.fireball_list:
                current_fireball_x = fireball[0]
                current_fireball_y = fireball[1]
                current_fireball_speed = fireball[2]
                current_fireball_index = fireball[3]
                image_fireball = self.image_fireball_list[int(current_fireball_index)]

                rect_fireball = image_fireball.get_rect()
                rect_fireball.x = current_fireball_x
                rect_fireball.y = current_fireball_y

                if rect_fireball.colliderect(rect_hero):
                    life_status = life_status - 1
                    pygame.time.delay(500)
                else:
                    temp_fireball_list.append([current_fireball_x, current_fireball_y,
                                               current_fireball_speed, current_fireball_index])

        self.fireball_list = temp_fireball_list.copy()


class Hero(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 4
        self.direction = 1
        self.flip = False
        self.image_index = 0
        self.image_axe_index = 0
        self.gravity = 0
        self.thrown_axe_list = list()
        self.cool_down_count = 0

        img_1 = pygame.image.load('graphics/viking_regular.png').convert_alpha()
        # img_1 = pygame.image.load('graphics/player_1.png').convert_alpha()
        img_1 = pygame.transform.scale(img_1,
                                       (int(img_1.get_width() * scale), int(img_1.get_height() * scale)))

        img_2 = pygame.image.load('graphics/viking_run.png').convert_alpha()
        # img_2 = pygame.image.load('graphics/player_2.png').convert_alpha()
        img_2 = pygame.transform.scale(img_2,
                                       (int(img_2.get_width() * scale), int(img_2.get_height() * scale)))
        self.image_list = [img_1, img_2]
        self.image = self.image_list[self.image_index]
        self.rect = self.image.get_rect()

        img = pygame.image.load('graphics/viking_attack.png').convert_alpha()
        self.image_attack = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))

        img_axe_1 = pygame.image.load('graphics/viking_axe_1.png').convert_alpha()
        img_axe_1 = pygame.transform.scale(img_axe_1,
                                           (int(img_axe_1.get_width() * scale), int(img_axe_1.get_height() * scale)))
        img_axe_2 = pygame.image.load('graphics/viking_axe_2.png').convert_alpha()
        img_axe_2 = pygame.transform.scale(img_axe_2,
                                           (int(img_axe_2.get_width() * scale), int(img_axe_2.get_height() * scale)))
        img_axe_3 = pygame.image.load('graphics/viking_axe_3.png').convert_alpha()
        img_axe_3 = pygame.transform.scale(img_axe_3,
                                           (int(img_axe_3.get_width() * scale), int(img_axe_3.get_height() * scale)))
        img_axe_4 = pygame.image.load('graphics/viking_axe_4.png').convert_alpha()
        img_axe_4 = pygame.transform.scale(img_axe_4,
                                           (int(img_axe_4.get_width() * scale), int(img_axe_4.get_height() * scale)))
        self.image_axe_list = [img_axe_1, img_axe_2, img_axe_3, img_axe_4]
        self.image_axe = self.image_axe_list[self.image_axe_index]
        self.rect_axe = self.image_axe.get_rect()

    def positioning(self, x, y):
        self.rect.center = (x, y)

    def move(self):
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

    def draw(self, moving_attack):
        self.gravity += 1
        self.rect.y += self.gravity

        # limit for bottom value
        if self.rect.bottom >= int(SCREEN_HEIGHT - self.image.get_height() - 15):
            self.rect.bottom = int(SCREEN_HEIGHT - self.image.get_height() - 15)

        # limit for top value
        if self.rect.top < 0:
            self.rect.top = 0

        # limit for left value
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > int(SCREEN_WIDTH / 2):
            self.rect.right = int(SCREEN_WIDTH / 2)

        # draw hero
        if moving_attack:
            screen.blit(pygame.transform.flip(self.image_attack, self.flip, False), self.rect)
            self.cooldown()
            if self.cool_down_count == 0:
                self.rect_axe.x = self.rect.x + 60
                self.rect_axe.y = self.rect.y + 20
                self.thrown_axe_list.append([self.rect.x + 60, self.rect.y + 20, self.direction, 0])
                self.cool_down_count = 1
        else:
            screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

        # draw axes
        temp_thrown_axe_list = list()
        if self.thrown_axe_list:
            temp_thrown_axe_list.clear()
            for thrown_axe in self.thrown_axe_list:
                current_thrown_axe_x = thrown_axe[0]
                current_thrown_axe_y = thrown_axe[1]
                current_thrown_axe_direction = thrown_axe[2]
                current_thrown_axe_index = thrown_axe[3]
                current_thrown_axe_index += 0.3
                if current_thrown_axe_index >= len(self.image_axe_list):
                    current_thrown_axe_index = 0
                image_axe = self.image_axe_list[int(current_thrown_axe_index)]

                rect_axe = image_axe.get_rect()
                rect_axe.x = 8 * current_thrown_axe_direction + current_thrown_axe_x
                current_thrown_axe_x = 8 * current_thrown_axe_direction + current_thrown_axe_x
                rect_axe.y = current_thrown_axe_y
                screen.blit(image_axe, rect_axe)

                if SCREEN_WIDTH > rect_axe.x > 0:
                    temp_thrown_axe_list.append([current_thrown_axe_x, current_thrown_axe_y,
                                                 current_thrown_axe_direction, current_thrown_axe_index])

            self.thrown_axe_list = temp_thrown_axe_list.copy()

    def cooldown(self):
        if self.cool_down_count >= 8:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1


class Menu(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    @staticmethod
    def draw_init():
        text_difficulty_level = menu_font.render(f'Please select difficulty level: ', False, 'Black').convert()
        text_easy = menu_font.render(f'Easy{easy_arrow}', False, 'Black').convert()
        text_medium = menu_font.render(f'Medium{medium_arrow}', False, 'Black').convert()
        text_hard = menu_font.render(f'Hard{hard_arrow}', False, 'Black').convert()

        screen.blit(text_difficulty_level, (int(SCREEN_WIDTH / 2) - 300, 100))
        screen.blit(text_easy, (int(SCREEN_WIDTH / 2) - 50, 300))
        screen.blit(text_medium, (int(SCREEN_WIDTH / 2) - 50, 400))
        screen.blit(text_hard, (int(SCREEN_WIDTH / 2) - 50, 500))

    @staticmethod
    def draw_win():
        text_win = menu_font.render(f'You WIN! Do you want to try again? (press y/Y)', False, 'White').convert()
        screen.blit(text_win, (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)))

    @staticmethod
    def draw_lose():
        text_lose = menu_font.render(f'You LOST! Do you want to try again? (press y/Y)', False, 'White').convert()
        screen.blit(text_lose, (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)))


# create background
bg = Background()

# create heart
hp = Heart()

# create boss
boss = Boss()
boss.positioning(int(SCREEN_WIDTH - (boss.image.get_width()/2)), int(SCREEN_HEIGHT - (boss.image.get_height()/2)) - 95)

# create hero
hero = Hero()
hero.positioning(int(hero.image.get_width()/2) + 100, int(SCREEN_HEIGHT - hero.image.get_height()) - 45)

run = True
while run:
    # draw background
    bg.draw()

    if game_init:
        Menu.draw_init()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if easy_arrow != '':
                        easy_arrow = ''
                        medium_arrow = ' <'
                        hard_arrow = ''
                    elif medium_arrow != '':
                        easy_arrow = ''
                        medium_arrow = ''
                        hard_arrow = ' <'
                    elif hard_arrow != '':
                        easy_arrow = ' <'
                        medium_arrow = ''
                        hard_arrow = ''

                if event.key == pygame.K_UP:
                    if easy_arrow != '':
                        easy_arrow = ''
                        medium_arrow = ''
                        hard_arrow = ' <'
                    elif medium_arrow != '':
                        easy_arrow = ' <'
                        medium_arrow = ''
                        hard_arrow = ''
                    elif hard_arrow != '':
                        easy_arrow = ''
                        medium_arrow = ' <'
                        hard_arrow = ''

                if event.key == pygame.K_RETURN:
                    if easy_arrow != '':
                        max_fireballs = 3
                    elif medium_arrow != '':
                        max_fireballs = 4
                    elif hard_arrow != '':
                        max_fireballs = 5

                    game_init = False
    else:

        boss.check_fireball_hit(hero.rect)

        # draw hp hearts
        hp.draw()

        # draw boss
        boss.draw()

        # draw hero
        hero.draw(moving_attack)
        hero.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_LALT:
                    hero.jump()
                if event.key == pygame.K_LSHIFT:
                    moving_attack = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_LSHIFT:
                    moving_attack = False

    # update everything
    pygame.display.update()
    clock.tick(60)


