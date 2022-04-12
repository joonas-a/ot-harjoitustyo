import pygame
#import entities
from level import Level
from game_loop import Application
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

def main():
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Platformer")

    level = Level()
    event_queue = EventQueue()
    renderer = Renderer(screen, level)
    clock = Clock()
    game_loop = Application(level, renderer, event_queue, clock)

    pygame.init()
    game_loop.run()


if __name__ == "__main__":
    main()