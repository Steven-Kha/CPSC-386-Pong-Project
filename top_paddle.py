# By Steven Kha 2018

import pygame
pygame.init()
from pygame.sprite import Sprite

class Top_Paddle(Sprite):

    def __init__(self, ai_settings, screen):
        """Create the Top_Paddle and set its starting position."""
        super(Top_Paddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.rect = pygame.Rect(0, 0, ai_settings.top_paddle_width,
                                ai_settings.top_paddle_height)

        self.screen_rect = screen.get_rect()

        self.color = ai_settings.top_paddle_color

        self.height = float(ai_settings.top_paddle_height)

        #Top_Paddle starts at top center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

        # print("Top Paddle position: " + str(self.rect))

        # Store a decimal value for the ship's center.
        self.x = float(self.rect.x)

        self.speed_factor = ai_settings.top_paddle_speed_factor

        # Movement flag for continuous movement
        self.moving_right = False
        self.moving_left = False

    def update(self, ai_settings):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.

        self.x += (ai_settings.top_paddle_x_direction *
                   ai_settings.top_paddle_speed_factor)
        self.rect.x = self.x

        #stop paddle from going off the top edge
        # Y axis gets smaller when it goes up!
        if self.moving_left and self.rect.top > 0:
            self.center -= self.ai_settings.top_paddle_speed_factor

            # ball.rect.x += ai_settings.ball_speed_factor
            #     ai_settings.ball_x_direction *= -1

            # print("Left Paddle position: " + str(self.rect))
            # print("self.rect.top: " + str(self.rect.top) + " > "
            #     "self.screen_rect.top: " + str(self.screen_rect.top))

        # stop paddle from going off the bottom edge y axis gettings
        # bigger when it moves down! When it reaches the end it is 800
        if self.moving_right and self.rect.bottom < 800:
            self.center += self.ai_settings.top_paddle_speed_factor

            # print("self.rect.bottom: " + str(self.rect.bottom) + "< 800")
            # print("Left Paddle position: " + str(self.rect))
        # Update rect object from self.center.

    def center_top_paddle(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.midright

    def check_edges(self):
        if self.rect.left <= 0:
            return True
        elif self.rect.right >= 1200:
            return True

    def draw_top_paddle(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
