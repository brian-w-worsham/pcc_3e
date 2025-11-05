import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        """This line positions the bullet’s rectangle so it starts exactly at
        the ship’s “midtop” anchor point. In Pygame, each Rect has named
        anchors (like center, midtop, midbottom, etc.) that represent specific
        points on the rectangle. Setting self.rect.midtop updates the bullet’s
        rect position so that its horizontal center aligns with the ship’s
        horizontal center, and its top edge sits at the same y-coordinate as
        the top edge of the ship. Width and height don’t change—only the
        position does."""
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
