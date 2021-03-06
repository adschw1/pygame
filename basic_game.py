import pygame

title = "Crossy RPG"
width = 800
height = 800
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:
    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(white)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        direction = 0
        player_character = PlayerChar('player.png', 375, 700, 50, 50)
        enemy_0 = EnemyChar('enemy.png', 20, 400, 50, 50)
        treasure = GameObject('treasure.png', 375, 100, 50, 50)

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Detect when key is pressed
                elif event.type == pygame.KEYDOWN:
                    # Move up
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Stop moving on release of key
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                # print(event)

            # Redraw screen
            self.screen.fill(white)

            # Draw treasure
            treasure.draw(self.screen)

            # Move and redraw the character
            player_character.move(direction, self.height)
            player_character.draw(self.screen)

            # Move enemy left to right
            enemy_0.move(self.width)
            enemy_0.draw(self.screen)

            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True

            pygame.display.update()
            clock.tick(self.TICK_RATE)
            # screen.blit(player_image, (375,375))
            # pygame.draw.rect(screen, black, [350, 350, 100, 100])
            # pygame.draw.circle(screen, black, (400, 300), 50)

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class PlayerChar(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False

        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True

class EnemyChar(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED

pygame.init()

new_game = Game(title, width, height)
new_game.run_game_loop()



pygame.quit()
quit()
