# # By Steven Kha 2018

import pygame
from pygame.sprite import Group
from left_paddle import Left_Paddle
from right_paddle import Right_Paddle
from bottom_paddle import Bottom_Paddle
from top_paddle import Top_Paddle

from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Super Pong 64")

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #make the left paddle
    left_paddle = Left_Paddle(ai_settings, screen)
    right_paddle = Right_Paddle(ai_settings, screen)
    bottom_paddle = Bottom_Paddle(ai_settings, screen)
    top_paddle = Top_Paddle(ai_settings, screen)

    balls = Group()

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        left_paddle, right_paddle, bottom_paddle, top_paddle, balls)

        if stats.game_active:
            left_paddle.update(ai_settings)
            right_paddle.update(ai_settings)
            bottom_paddle.update(ai_settings)
            top_paddle.update(ai_settings)

            gf.update_balls(ai_settings, stats, screen, sb, left_paddle,
                right_paddle, bottom_paddle, top_paddle, balls)

            gf.update_top_paddle(ai_settings, stats, screen, sb, left_paddle,
                right_paddle, bottom_paddle, top_paddle, balls)

        gf.update_screen(ai_settings, screen, stats, sb, left_paddle, right_paddle,
                 bottom_paddle, top_paddle, balls, play_button)


run_game()
