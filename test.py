import pygame
import os

class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)

        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        self.position = position

    def update(self):
        rect_center = self.position + self.offset
        self.rect = self.image.get_rect(center=rect_center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3)
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5)


class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)


def setup_gemstone():
    small_gold = Gemstone(gemstone_images[0],(200, 380))
    gemstone_group.add(small_gold)

    gemstone_group.add(Gemstone(gemstone_images[1],(300, 500)))
    gemstone_group.add(Gemstone(gemstone_images[2],(300, 380)))
    gemstone_group.add(Gemstone(gemstone_images[3],(900, 420)))


pygame.init()
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")
clock = pygame.time.Clock()

default_offset_x_claw = 40

RED = (255, 0, 0)
BLACK = (0, 0, 0)

def load_image(filename):
    current_path = os.path.realpath('.')
    print("Current path:" + current_path)
    img = pygame.image.load(os.path.join(current_path, filename))
    return img

background = load_image("bg.png")
gemstone_images = [
    load_image("small_gold.png"),
    load_image("big_gold.png"),
    load_image("stone.png"),
    load_image("diamond.png"),
]

gemstone_group = pygame.sprite.Group()
setup_gemstone()

claw_image = load_image("claw.png")
claw = Claw(claw_image, (screen_width//2, 110))

running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    gemstone_group.draw(screen)

    claw.update()
    claw.draw(screen)

    pygame.display.update()

pygame.quit()
