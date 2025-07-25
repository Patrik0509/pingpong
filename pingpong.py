from pygame import *

# настройка сцены

background_color = (200,255,255)
win_width = 700
win_height  = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        


#создание и настройка окна
window = display.set_mode((win_width, win_height))
window.fill(background_color)

#создание объектов
ball = GameSprite('ball.png',200,200,50,50,4)
player1 = Player('racket.png',30,200,50,150,4)
player2 = Player('racket.png',520,200,50,150,4)

speed_x = 4
speed_y = 4

font.init()
font1 = font.Font(None,35)
lose1 = font1.render('Игрок 1 проиграл',True,(180,0,0))
lose2 = font1.render('Игрок 2    проиграл',True,(180,0,0))
#вспомогательные параметры
game = True
finish = False
clock = time.Clock()

#игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(background_color)
        player1.update_left()       
        player2.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
            game = True

        if ball.rect.x < 0:
            finish = True
            window.blit(lose2,(200,200))
            game = True

        player1.reset()
        player2.reset()       
        ball.reset()
    display.update()
    clock.tick(60)