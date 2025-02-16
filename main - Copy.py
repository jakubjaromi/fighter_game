import pygame
from sys import exit
import random
#
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
# game_active = False
# game_init = True
# pygame.init()
# pygame.display.set_caption('Runner')
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# clock = pygame.time.Clock()
# game_font = pygame.font.Font('font/Minecraft.ttf', 60)
# counter = 0
#
# background_surface = pygame.image.load('graphics/background.jpg').convert()
# text_surface = game_font.render('Press SPACE to start', False, 'Black').convert()
# # player_surface = pygame.image.load('graphics/player_no_bg.png').convert_alpha()
# player_surface = pygame.image.load('graphics/player_girl_no_bg.png').convert_alpha()
# monster_surface = pygame.image.load('graphics/spider_no_bg.png').convert_alpha()
# bee_1_surface = pygame.image.load('graphics/bee_no_bg.png').convert_alpha()
# bee_2_surface = pygame.image.load('graphics/bee_no_bg.png').convert_alpha()
# bee_3_surface = pygame.image.load('graphics/bee_no_bg.png').convert_alpha()
# bee_4_surface = pygame.image.load('graphics/bee_no_bg.png').convert_alpha()
# bee_5_surface = pygame.image.load('graphics/bee_no_bg.png').convert_alpha()
# dragon_surface = pygame.image.load('graphics/dragon_no_bg.png').convert_alpha()
#
# text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2, 50))
#
# background_surface = pygame.transform.scale(background_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
# player_surface = pygame.transform.scale(player_surface, (60, 100))
# monster_surface = pygame.transform.scale(monster_surface, (70, 40))
# bee_1_surface = pygame.transform.scale(bee_1_surface, (70, 40))
# bee_2_surface = pygame.transform.scale(bee_2_surface, (70, 40))
# bee_3_surface = pygame.transform.scale(bee_3_surface, (70, 40))
# bee_4_surface = pygame.transform.scale(bee_4_surface, (70, 40))
# bee_5_surface = pygame.transform.scale(bee_5_surface, (70, 40))
# dragon_surface = pygame.transform.scale(dragon_surface, (200, 120))
#
# player_rect = player_surface.get_rect(topleft=(40, 750))
# monster_rect = monster_surface.get_rect(topleft=(SCREEN_WIDTH, 800))
# bee_1_rect = bee_1_surface.get_rect(topleft=(SCREEN_WIDTH, 200))
# bee_2_rect = bee_2_surface.get_rect(topleft=(SCREEN_WIDTH, 100))
# bee_3_rect = bee_3_surface.get_rect(topleft=(SCREEN_WIDTH, 300))
# bee_4_rect = bee_4_surface.get_rect(topleft=(SCREEN_WIDTH, 500))
# bee_5_rect = bee_5_surface.get_rect(topleft=(SCREEN_WIDTH, 650))
# dragon_rect = dragon_surface.get_rect(topleft=(SCREEN_WIDTH, 400))
#
# player_gravity = 0
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#
#         if game_active:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     player_gravity = - 15
#
#         else:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     game_active = True
#                     game_init = False
#                     monster_rect.left = SCREEN_WIDTH
#                     bee_1_rect.left = SCREEN_WIDTH
#                     bee_2_rect.left = SCREEN_WIDTH
#                     bee_3_rect.left = SCREEN_WIDTH
#                     bee_4_rect.left = SCREEN_WIDTH
#                     bee_5_rect.left = SCREEN_WIDTH
#                     dragon_rect.left = SCREEN_WIDTH
#                     counter = 0
#
#     if game_active:
#         # draw all elements
#         counter += 1
#         screen.blit(background_surface, (0, 0))
#         text_surface_score = game_font.render(f'Score: {counter}', False, 'Black').convert()
#         text_rect_score = text_surface_score.get_rect(center=(SCREEN_WIDTH / 2, 50))
#         screen.blit(text_surface_score, text_rect_score)
#
#         player_gravity += 1
#         player_rect.y += player_gravity
#         if player_rect.bottom >= 850:
#             player_rect.bottom = 850
#
#         # player_rect.left += 1
#
#         if player_rect.top < 0:
#             player_rect.top = 0
#
#         screen.blit(player_surface, player_rect)
#
#         # monster_x_pos -= 10
#         # if monster_x_pos < -100:
#         #     monster_x_pos = SCREEN_WIDTH
#         # screen.blit(monster_surface, (monster_x_pos, 780))
#
#         # spider
#         screen.blit(monster_surface, monster_rect)
#         monster_rect.right -= 20
#         if monster_rect.right <= 0:
#             monster_rect.left = SCREEN_WIDTH
#
#         if monster_rect.colliderect(player_rect):
#             game_active = False
#
#         if game_active:
#             # dragon
#             screen.blit(dragon_surface, dragon_rect)
#             dragon_rect.right -= 5
#             if dragon_rect.right <= 0:
#                 dragon_rect.left = SCREEN_WIDTH
#                 dragon_rect.bottom = random.randint(50, 800)
#
#             if dragon_rect.colliderect(player_rect):
#                 game_active = False
#
#         if game_active:
#             # bee1
#             screen.blit(bee_1_surface, bee_1_rect)
#             bee_1_rect.right -= 12
#             if bee_1_rect.right <= 0:
#                 bee_1_rect.left = SCREEN_WIDTH
#                 bee_1_rect.bottom = random.randint(50, 800)
#
#             if bee_1_rect.colliderect(player_rect):
#                 game_active = False
#
#         if game_active:
#             # bee2
#             screen.blit(bee_2_surface, bee_2_rect)
#             bee_2_rect.right -= 8
#             if bee_2_rect.right <= 0:
#                 bee_2_rect.left = SCREEN_WIDTH
#                 bee_2_rect.bottom = random.randint(50, 800)
#
#             if bee_2_rect.colliderect(player_rect):
#                 game_active = False
#
#         if game_active:
#             # bee3
#             screen.blit(bee_3_surface, bee_3_rect)
#             bee_3_rect.right -= 14
#             if bee_3_rect.right <= 0:
#                 bee_3_rect.left = SCREEN_WIDTH
#                 bee_3_rect.bottom = random.randint(50, 800)
#
#             if bee_3_rect.colliderect(player_rect):
#                 game_active = False
#
#         if game_active:
#             # bee4
#             screen.blit(bee_4_surface, bee_4_rect)
#             bee_4_rect.right -= 7
#             if bee_4_rect.right <= 0:
#                 bee_4_rect.left = SCREEN_WIDTH
#                 bee_4_rect.bottom = random.randint(50, 800)
#
#             if bee_4_rect.colliderect(player_rect):
#                 game_active = False
#
#         if game_active:
#             # bee5
#             screen.blit(bee_5_surface, bee_5_rect)
#             bee_5_rect.right -= 11
#             if bee_5_rect.right <= 0:
#                 bee_5_rect.left = SCREEN_WIDTH
#                 bee_5_rect.bottom = random.randint(50, 800)
#
#             if bee_5_rect.colliderect(player_rect):
#                 game_active = False
#
#     else:
#         screen.blit(background_surface, (0, 0))
#         screen.blit(player_surface, player_rect)
#         screen.blit(monster_surface, monster_rect)
#         screen.blit(dragon_surface, dragon_rect)
#         screen.blit(bee_1_surface, bee_1_rect)
#         screen.blit(bee_2_surface, bee_2_rect)
#         screen.blit(bee_3_surface, bee_3_rect)
#         screen.blit(bee_4_surface, bee_4_rect)
#         screen.blit(bee_5_surface, bee_5_rect)
#         if game_init:
#             screen.blit(text_surface, text_rect)
#         else:
#             text_surface_game_over = game_font.render(f'Your score: {counter}. Press SPACE to try again', False,
#                                                       'Black').convert()
#             text_rect_game_over = text_surface_game_over.get_rect(center=(SCREEN_WIDTH / 2, 50))
#             screen.blit(text_surface_game_over, text_rect_game_over)
#
#
#     # update everything
#     pygame.display.update()
#     clock.tick(60)


class JumperGame:

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Jumper Game')

        # variables
        self.screen = pygame.display.set_mode((JumperGame.SCREEN_WIDTH, JumperGame.SCREEN_HEIGHT))
        self.game_font = pygame.font.Font('font/Minecraft.ttf', 60)
        self.clock = pygame.time.Clock()

        self.bg_x = 0
        self.player_index = 0
        self.player_x = int(JumperGame.SCREEN_WIDTH / 2)
        self.player_y = 670

        # begin
        self.launch_game()

    def launch_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # update everything
            self.provide_background()
            self.provide_player()
            pygame.display.update()
            self.clock.tick(60)

    def provide_background(self):
        bg_surface = pygame.image.load('graphics/bg.jpg').convert()
        bg_surface = pygame.transform.scale(bg_surface, (JumperGame.SCREEN_WIDTH, JumperGame.SCREEN_HEIGHT))
        self.screen.blit(bg_surface, (self.bg_x, 0))
        self.screen.blit(bg_surface, (JumperGame.SCREEN_WIDTH + self.bg_x, 0))
        if self.bg_x == -JumperGame.SCREEN_WIDTH:
            self.screen.blit(bg_surface, (JumperGame.SCREEN_WIDTH + self.bg_x, 0))
            self.bg_x = 0
        self.bg_x -= 5

    def provide_player(self, jump_action=False):
        if jump_action:
            player_surface = pygame.image.load('graphics/player_1.png').convert_alpha()
        else:
            player_walk_1 = pygame.image.load('graphics/player_1.png').convert_alpha()
            player_walk_2 = pygame.image.load('graphics/player_2.png').convert_alpha()
            player_walk = [player_walk_1, player_walk_2]
            self.player_index += 0.1
            if self.player_index >= len(player_walk):
                self.player_index = 0
            player_surface = player_walk[int(self.player_index)]
        self.screen.blit(player_surface, (self.player_x, self.player_y))


if __name__ == '__main__':
    JumperGame()
