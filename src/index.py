import pygame
import entities
from game_loop import Application
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

def main():
    width = 720
    height = 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Platformer")

    player = entities.Player()
    floor = entities.Floor()
    event_queue = EventQueue()
    renderer = Renderer(screen, entities)
    clock = Clock()
    game_loop = Application(player, floor, renderer, event_queue, clock)

    pygame.init()
    game_loop.run()


if __name__ == "__main__":
    main()