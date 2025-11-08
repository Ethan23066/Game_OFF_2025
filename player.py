from settings_game import WIDTH

class Player:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, 580))
        self.speed = 5

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_position(self):
        return self.rect.center

    def fire(self):
        # Optionnel : retourne un bullet à partir du centre
        from bullet import Bullet
        return Bullet(self.rect.centerx, self.rect.top)
