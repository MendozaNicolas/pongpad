import pygame
import sys

# Game constants
SCREEN_WIDTH = 1008
SCREEN_HEIGHT = 496
BALL_SIZE = 20
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 160
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pygame initialization
pygame.init()

ICON = pygame.image.load('assets/icon.png')
BACKGROUND = pygame.image.load('assets/notepad.png')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_icon(ICON)
pygame.display.set_caption('*Sin título: Bloc de notas')
clock = pygame.time.Clock()

PADDLEDESIGN = [
    "|   |",
    "|   |",
    "|   |",
    "|   |",
    "|   |",
    "|   |",
    "|   |"
]


BALL= "O"

# Create a font object
object_font = pygame.font.Font(None, 24)
# Font for score
font = pygame.font.Font(None, 36)


# Paddle class
class Paddle(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 5

    def move_up(self):
        if self.top > 25:
            self.y -= self.speed

    def move_down(self):
        if self.bottom < SCREEN_HEIGHT-40:
            self.y += self.speed

# Ball class
class Ball(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.top < 20 or self.bottom > (SCREEN_HEIGHT-30):
            self.speed_y *= -1
        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.speed_x *= -1

    def reset(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.speed_x *= -1

# Create paddles and ball
paddle1 = Paddle(10, (SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2))
paddle2 = Paddle(SCREEN_WIDTH - 35, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2)
ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



# Score variables
score1 = 0
score2 = 0

# Bot variables
bot_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move_up()
    if keys[pygame.K_s]:
        paddle1.move_down()

    # Bot movement
    if ball.x > SCREEN_WIDTH / 2 and ball.speed_x > 0:
        if ball.y < paddle2.y:
            paddle2.move_up()
        elif ball.y > paddle2.y + PADDLE_HEIGHT:
            paddle2.move_down()

    ball.move()

    # Collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball.speed_x *= -1

    # Score and reset
    if ball.left < 0:
        score2 += 1
        ball.reset()
    elif ball.right > SCREEN_WIDTH:
        score1 += 1
        ball.reset()

    # Draw everything
    screen.fill(WHITE)

    # Render the ASCII art and get a surface
    screen.blit(BACKGROUND, (0,0))
    for i, line in enumerate(PADDLEDESIGN):
        paddle1_surface = object_font.render(line, True, (0, 0, 0))
        paddle2_surface = object_font.render(line, True, (0, 0, 0))
        screen.blit(paddle1_surface, (paddle1.x, paddle1.y + i * 24))
        screen.blit(paddle2_surface, (paddle2.x, paddle2.y + i * 24))


    # HITBOX
    # pygame.draw.rect(screen, (255, 0, 0), paddle1, 2)  
    # pygame.draw.rect(screen, (255, 0, 0), paddle2, 2)  

    # Draw the ball
    ball_surface = object_font.render(BALL, True, (0, 0, 0))
    screen.blit(ball_surface, ball.topleft)



    # Draw score
    score_text = font.render(f"{score1} - {score2}", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH / 2 - 20, 30))

    pygame.display.flip()
    clock.tick(FPS)