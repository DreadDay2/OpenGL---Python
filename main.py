import pygame
import moderngl
import sys
from model_of_game import *
from camera import Camera
from map import *

pygame.display.set_caption("Catch a sasuage !")
WHITE = (255, 255, 255)
FPS = 60


class GraphicEngine:
    def __init__(self, WINDOWS_SIZE=(900, 500)):
        pygame.init()
        self.WINDOW_SIZE = WINDOWS_SIZE
        # ustawianie atrybutów opengl
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        # tworzenie kontekstu opengl
        pygame.display.set_mode(
            self.WINDOW_SIZE, flags=pygame.OPENGL | pygame.DOUBLEBUF)
        # wykrywanie i wykorzystanie kontekstu opengl
        self.ctx = moderngl.create_context()
        self.ctx.enable(flags=moderngl.DEPTH_TEST)
        # tworzenie timera obiektu
        self.clock = pygame.time.Clock()
        self.time = 0
        # kamera gracza
        self.camera = Camera(self)
        # scena
        self.scene = Cube(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.scene.destroy()
                pygame.quit()
                sys.exit()

    def render(self):
        # czyszczenie buforu ramki i ustawienie koloru okna
        self.ctx.clear(color=(255, 255, 255))
        # renderowanie naszej sceny
        self.scene.render()
        # zmienianie buforu
        pygame.display.flip()

    def get_time(self):
        self.time = pygame.time.get_ticks() * 0.001

    def run_game(self):
        while True:
            self.get_time()
            self.check_events()
            self.render()
            self.clock.tick(60)


if __name__ == '__main__':
    game = GraphicEngine()
    game.run_game()
