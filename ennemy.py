from settings_game import WIDTH

class Enemy:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.direction = 1  # 1 = droite, -1 = gauche

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 20  # descend à chaque rebond

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
