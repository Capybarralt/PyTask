# import pygame
# import random
# from os import path
# from pygame.locals import *
#
# img_dir = path.join(path.dirname(__file__), 'img')
# snd_dir = path.join(path.dirname(__file__), 'snd')
#
# WIDTH = 600
# HEIGHT = 600
# BAR_LENGTH = 100
# BAR_HEIGHT = 10
# FPS = 60
# POWERUP_TIME = 5000
# SCORE = 0.5
#
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
#
# # Создаем игру и окно
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("STARFIGHT!")
# clock = pygame.time.Clock()
#
# font_name = pygame.font.match_font('arial')
#
#
# def draw_text(surf, text, size, x, y):
#     font = pygame.font.Font(font_name, size)
#     text_surface = font.render(text, True, WHITE)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x, y)
#     surf.blit(text_surface, text_rect)
#
#
# def newmob():
#     m = Mob()
#     all_sprites.add(m)
#     mobs.add(m)
#
#
# def draw_shield_bar(surf, x, y, pct):
#     if pct < 0:
#         pct = 0
#     fill = (pct / 100) * BAR_LENGTH
#     outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
#     fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
#     pygame.draw.rect(surf, GREEN, fill_rect)
#     pygame.draw.rect(surf, WHITE, outline_rect, 2)
#
#
# def draw_lives(surf, x, y, lives, img):
#     for i in range(lives):
#         img_rect = img.get_rect()
#         img_rect.x = x + 30 * i
#         img_rect.y = y
#         surf.blit(img, img_rect)
#
#
# def show_go_screen():
#     screen.blit(background, background_rect)
#     draw_text(screen, "STARFIGHT", 64, WIDTH / 2, HEIGHT / 4)
#     draw_text(screen, "ARROW keys move, SPACE to fire, ESCAPE to pause", 22,
#               WIDTH / 2, HEIGHT / 2)
#     draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
#     with open('maxscore.txt', 'r') as f:
#         max = f.read()
#     draw_text(screen, f"max score {max}", 18, WIDTH / 2, HEIGHT * 1 / 3 + 30)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if event.type == pygame.KEYUP:
#                 waiting = False
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.transform.scale(player_img, (50, 38))
#         self.image.set_colorkey(BLACK)
#         self.rect = self.image.get_rect()
#         self.radius = 20
#         self.rect.centerx = WIDTH / 2
#         self.rect.centery = HEIGHT - 40
#         self.speedx = 0
#         self.speedx = 0
#         self.shield = 100
#         self.shoot_delay = 500
#         self.last_shot = pygame.time.get_ticks()
#         self.lives = 3
#         self.hidden = False
#         self.hide_timer = pygame.time.get_ticks()
#         self.power = 1
#         self.power_time = pygame.time.get_ticks()
#
#     def update(self):
#         if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
#             self.power -= 1
#             self.power_time = pygame.time.get_ticks()
#
#         if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
#             self.hidden = False
#             self.rect.centerx = WIDTH / 2
#             self.rect.bottom = HEIGHT - 10
#
#         self.speedx = 0
#         self.speedy = 0
#         keystate = pygame.key.get_pressed()
#         if keystate[pygame.K_LEFT]:
#             self.speedx = -8
#         if keystate[pygame.K_RIGHT]:
#             self.speedx = 8
#         if keystate[pygame.K_UP]:
#             self.speedy = -8
#         if keystate[pygame.K_DOWN]:
#             self.speedy = 8
#
#         if keystate[pygame.K_SPACE]:
#             self.shoot()
#
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#         if self.rect.right > WIDTH:
#             self.rect.right = WIDTH
#         if self.rect.left < 0:
#             self.rect.left = 0
#         if self.rect.top <= 0:
#             self.rect.top = 0
#         if self.rect.bottom >= HEIGHT:
#             self.rect.bottom = HEIGHT
#
#     def powerup(self):
#         self.power += 1
#         self.power_time = pygame.time.get_ticks()
#
#     def shoot(self):
#         now = pygame.time.get_ticks()
#         if now - self.last_shot > self.shoot_delay:
#             self.last_shot = now
#             if self.power == 1:
#                 bullet = Bullet(self.rect.centerx, self.rect.top, -10)
#                 all_sprites.add(bullet)
#                 bullets.add(bullet)
#                 shoot_sound.play()
#             if self.power >= 2:
#                 bullet1 = Bullet(self.rect.left, self.rect.centery, -10)
#                 bullet2 = Bullet(self.rect.right, self.rect.centery, -10)
#                 all_sprites.add(bullet1)
#                 all_sprites.add(bullet2)
#                 bullets.add(bullet1)
#                 bullets.add(bullet2)
#                 shoot_sound.play()
#
#     def hide(self):
#         # временно скрыть игрока
#         self.hidden = True
#         self.hide_timer = pygame.time.get_ticks()
#         self.rect.center = (WIDTH / 2, HEIGHT + 200)
#
#
# class FlyMobs(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.transform.scale(flymob_img, (50, 38))
#         self.image.set_colorkey(BLACK)
#         self.rect = self.image.get_rect()
#         self.radius = 20
#         # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
#         self.rect.centerx = WIDTH / 2
#         self.rect.bottom = 50
#         self.speedy = random.randrange(1, 5)
#         self.speedx = random.randrange(-2, 2)
#         self.shoot_delay = 1000
#         self.last_shot = pygame.time.get_ticks()
#
#
#     def update(self):
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#
#         if self.rect.bottom >= HEIGHT / 2 or self.rect.top <= 0:
#             self.speedy = -self.speedy
#         if self.rect.left <= 0 or self.rect.right >= WIDTH:
#             self.speedx = -self.speedx
#
#         self.shoot()
#
#
#     def shoot(self):
#         now = pygame.time.get_ticks()
#         if now - self.last_shot > self.shoot_delay:
#             self.last_shot = now
#             bullet = Bullet(self.rect.centerx, self.rect.bottom + 20, 10)
#             all_sprites.add(bullet)
#             mob_bullets.add(bullet)
#             shoot_sound.play()
#
#
# class Mob(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image_orig = random.choice(meteor_images)
#         self.image_orig.set_colorkey(BLACK)
#         self.image = self.image_orig.copy()
#         self.rect = self.image.get_rect()
#         self.radius = int(self.rect.width * .85 / 2)
#         self.rect.x = random.randrange(WIDTH - self.rect.width)
#         self.rect.y = random.randrange(-150, -100)
#         self.speedy = random.randrange(1, 8)
#         self.speedx = random.randrange(-3, 3)
#         self.rot = 0
#         self.rot_speed = random.randrange(-8, 8)
#         self.last_update = pygame.time.get_ticks()
#
#     def rotate(self):
#         now = pygame.time.get_ticks()
#         if now - self.last_update > 50:
#             self.last_update = now
#             self.rot = (self.rot + self.rot_speed) % 360
#             new_image = pygame.transform.rotate(self.image_orig, self.rot)
#             old_center = self.rect.center
#             self.image = new_image
#             self.rect = self.image.get_rect()
#             self.rect.center = old_center
#
#     def update(self):
#         self.rotate()
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#         if self.rect.top > HEIGHT + 10 or self.rect.right <= 0 or self.rect.left >= WIDTH:
#             self.rect.x = random.randrange(WIDTH - self.rect.width)
#             self.rect.y = random.randrange(-100, -40)
#             self.speedy = random.randrange(1, 8)
#
#
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y, speedy):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = bullet_img
#         self.image.set_colorkey(BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.bottom = y
#         self.rect.centerx = x
#         self.speedy = speedy
#
#     def update(self):
#         self.rect.y += self.speedy
#         # убить, если он заходит за верхнюю часть экрана
#         if self.rect.bottom < 0:
#             self.kill()
#
#
# class Pow(pygame.sprite.Sprite):
#     def __init__(self, center):
#         pygame.sprite.Sprite.__init__(self)
#         self.type = random.choice(['shield', 'gun'])
#         self.image = powerup_images[self.type]
#         self.image.set_colorkey(BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.center = center
#         self.speedy = 2
#
#     def update(self):
#         self.rect.y += self.speedy
#         if self.rect.top > HEIGHT:
#             self.kill()
#
#
# class Explosion(pygame.sprite.Sprite):
#     def __init__(self, center, size):
#         pygame.sprite.Sprite.__init__(self)
#         self.size = size
#         self.image = explosion_anim[self.size][0]
#         self.rect = self.image.get_rect()
#         self.rect.center = center
#         self.frame = 0
#         self.last_update = pygame.time.get_ticks()
#         self.frame_rate = 50
#
#     def update(self):
#         now = pygame.time.get_ticks()
#         if now - self.last_update > self.frame_rate:
#             self.last_update = now
#             self.frame += 1
#             if self.frame == len(explosion_anim[self.size]):
#                 self.kill()
#             else:
#                 center = self.rect.center
#                 self.image = explosion_anim[self.size][self.frame]
#                 self.rect = self.image.get_rect()
#                 self.rect.center = center
#
#
# # Загрузка игровой графики
# background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
# background = pygame.transform.scale(background, (WIDTH, HEIGHT))
# background_rect = background.get_rect()
#
# player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
# player_mini_img = pygame.transform.scale(player_img, (25, 19))
# player_mini_img.set_colorkey(BLACK)
#
# flymob_img = pygame.image.load(path.join(img_dir, "player2.png")).convert()
#
# bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
#
# meteor_images = []
# meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',
#                'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
#                'meteorBrown_tiny1.png']
# for img in meteor_list:
#     meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())
#
# pygame.mouse.set_visible(False)
#
# explosion_anim = {}
# explosion_anim['lg'] = []
# explosion_anim['sm'] = []
# explosion_anim['player'] = []
# for i in range(9):
#     filename = 'regularExplosion0{}.png'.format(i)
#     img = pygame.image.load(path.join(img_dir, filename)).convert()
#     img.set_colorkey(BLACK)
#     img_lg = pygame.transform.scale(img, (75, 75))
#     explosion_anim['lg'].append(img_lg)
#     img_sm = pygame.transform.scale(img, (32, 32))
#     explosion_anim['sm'].append(img_sm)
#     filename = 'sonicExplosion0{}.png'.format(i)
#     img = pygame.image.load(path.join(img_dir, filename)).convert()
#     img.set_colorkey(BLACK)
#     explosion_anim['player'].append(img)
#
# powerup_images = {}
# powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
# powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()
#
#
# # Загрузка мелодий игры
# shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
# shield_sound = pygame.mixer.Sound(path.join(snd_dir, 'pow4.wav'))
# power_sound = pygame.mixer.Sound(path.join(snd_dir, 'pow5.wav'))
# expl_sounds = []
# for snd in ['expl3.wav', 'expl6.wav']:
#     expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
#
# create_score = 500
# pause = False
#
# # Цикл игры
# game_over = True
# running = True
# while running:
#     if game_over:
#         show_go_screen()
#         game_over = False
#         all_sprites = pygame.sprite.Group()
#         mobs = pygame.sprite.Group()
#         bullets = pygame.sprite.Group()
#         mob_bullets = pygame.sprite.Group()
#         powerups = pygame.sprite.Group()
#         player = Player()
#         all_sprites.add(player)
#
#         for i in range(4):
#             newmob()
#         score = 0
#
#     score += SCORE
#
#     if score > create_score:
#         for i in range(2):
#             flymob = FlyMobs()
#             all_sprites.add(flymob)
#             mobs.add(flymob)
#         create_score += 500
#
#     # Держим цикл на правильной скорости
#     clock.tick(FPS)
#     # Ввод процесса (события)
#     for event in pygame.event.get():
#         # проверка для закрытия окна
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == KEYUP:
#             if event.key == K_p:
#                 pause = True
#                 while pause:
#
#                     for event in pygame.event.get():
#                         if event.type == KEYUP:
#                             if event.key == K_p:
#                                 pause = False
#
#     # Обновление
#     all_sprites.update()
#
#     # проверьте, не попала ли пуля в моб
#     hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
#     for hit in hits:
#         #score += 50 - hit.radius
#         random.choice(expl_sounds).play()
#         expl = Explosion(hit.rect.center, 'lg')
#         all_sprites.add(expl)
#         if random.random() > 0.9:
#             pow = Pow(hit.rect.center)
#             all_sprites.add(pow)
#             powerups.add(pow)
#         newmob()
#
#
#     #  Проверка, не ударил ли моб игрока
#     hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
#     for hit in hits:
#         player.shield -= hit.radius * 2
#         expl = Explosion(hit.rect.center, 'sm')
#         all_sprites.add(expl)
#         newmob()
#         if player.shield <= 0:
#             death_explosion = Explosion(player.rect.center, 'player')
#             all_sprites.add(death_explosion)
#             player.hide()
#             player.lives -= 1
#             player.shield = 100
#
#     # Проверка попал ли выстрел в игрока
#     hits = pygame.sprite.spritecollide(player, mob_bullets, True, pygame.sprite.collide_circle)
#     for hit in hits:
#         player.shield -= 30
#         expl = Explosion(hit.rect.center, 'sm')
#         all_sprites.add(expl)
#         if player.shield <= 0:
#             death_explosion = Explosion(player.rect.center, 'player')
#             all_sprites.add(death_explosion)
#             player.hide()
#             player.lives -= 1
#             player.shield = 100
#
#
#     # Проверка столкновений игрока и улучшения
#     hits = pygame.sprite.spritecollide(player, powerups, True)
#     for hit in hits:
#         if hit.type == 'shield':
#             player.shield += random.randrange(10, 30)
#             if player.shield >= 100:
#                 player.shield = 100
#         if hit.type == 'gun':
#             player.powerup()
#             power_sound.play()
#
#     # Если игрок умер, игра окончена
#     if player.lives == 0 and not death_explosion.alive():
#         with open('maxscore.txt', 'r') as f:
#             max = f.read()
#         if int(score) > int(max):
#             with open('maxscore.txt', 'w') as f:
#                 f.write(str(int(score)))
#         create_score = 500
#         game_over = True
#
#     # Рендеринг
#     screen.fill(BLACK)
#     screen.blit(background, background_rect)
#     all_sprites.draw(screen)
#     draw_text(screen, str(int(score)), 18, WIDTH / 2, 10)
#     draw_shield_bar(screen, 5, 5, player.shield)
#     draw_lives(screen, WIDTH - 100, 5, player.lives,
#                player_mini_img)
#     # После отрисовки всего, переворачиваем экран
#     pygame.display.flip()
#
# pygame.quit()

import random
# M = []
# S = []
# M1 = []
# n = 51504
# e = 451
# d = 571
#
# for i in range(10):
#     M.append(random.randrange(1000, 100000, 1))
#
# print('Исходные\n', M)
#
# for i in M:
#     S.append((i ** d) % n)
#
# print('Зашифрованные\n', S)
#
# for i in S:
#     M1.append((i ** e) % n)
#
# print('Проверка\n', M1)

# p = 966115223
# p = 966115223
# a = 29
# x = 10381
# y = a ** x % p
# print(y)
#
#
# def nod(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#
#     return a + b
#
# rand = []
# for i in range(10000, 100000):
#     if nod(i, p - 1):
#         rand.append(i)
#
# k = []
# R = []
# T = []
# C = []
# Z = []
# T1 = []
# for i in range(10):
#     T.append(random.randrange(10000, 1000000))
#     k.append(random.choice(rand))
#     R.append(a ** k[i] % p)
#     C.append(y ** k[i] * T[i] % p)
#     T1.append(1)
#
# print('T\n', T)
# print('k\n', k)
# print('R\n', R)
# print('C\n', C)
# print('T\n', T)
# print('Z-1\n', Z)
# print('T1\n', T1)

#print(455419988 ** 58099 % 966115223)
# k = 0
#
# p = 966115223
# a = 16657159
# x = []
# y = []
# for i in range(10):
#     x.append(random.randrange(10000, 100000, 1))
#     y.append(a ** x[i] % p)
#
# for i in range(10):
#     for j in range(10):
#         if (y[i] ** x[j] % p == y[j] ** x[i] % p):
#             continue
#         else:
#             k += 1
#
# print(x, '\n', y)
#
# if k == 0:
#     print('Условаие выполняется')
# else:
#     print('Условаие не выполняется')

# p = 347
# q = 563
# n = p * q
# M = 12464 #random.randomrange(0, n, 1)
# c = M ** 2 % n
#
# mp1 = c ** ((p + 1) / 4) % p
# mp2 = p - mp1
# mq1 = c ** ((q + 1) / 4) % q
# mq2 = q - mq1
#
# a = q * (q ** (-1) % p)
# print(a)

print(29 ** (-1) % 966115223)