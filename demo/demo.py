import pygame
from pygame.locals import *
from engine.app import GAPP
from valley.world import GridWorld


class App(GAPP):
    def __init__(self):
        super(App, self).__init__()
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 480
        self.fps = 30

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill((0, 0, 0))
        pygame.display.set_caption('NPCValley')
        self._clock = pygame.time.Clock()
        self.setup()
        self._running = True

    def setup(self):
        GridWorld((10, 10))

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.lock()
        for i in range(60):
            for j in range(40):
                pygame.draw.rect(self._display_surf, (255, 255, 255), pygame.Rect(i * 10, j * 10, 8, 8))
        self._display_surf.unlock()
        pygame.display.update()
        self._clock.tick(30)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def on_key_down(self, event):
        if event.key == K_ESCAPE:
            self._running = False


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
