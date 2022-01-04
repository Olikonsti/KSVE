from KSVE.GLOBAL import *
from KSVE.UTILS.logger import *
from KSVE.Event import *

import pygame

class Engine():
    def __init__(self, debug: bool = False):

        self.DEBUG = debug
        self.VERSION = 0.1
        self.LOGLEVEL = "INFO"
        self.FPS = 90
        KSVE_ENGINE_INSTANCE[0] = self
        print(f"You are using KSV Engine 2.0 Version {self.VERSION} with pygame and pymunk")

        initLog(self.LOGLEVEL, self.DEBUG)

        pygame.init()
        self._screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("KSVE Window")

        self.active_view = None
        self.events = []

        loginfo("Engine started")

        self.clock = pygame.time.Clock()
        self.tick = 0

        self.print_event_count()

    def set_active_view(self, view):
        self.active_view = view

    def print_event_count(self):
        if len(self.events) > 1:
            loginfo(f"Engine Event count: {len(self.events)}")
        Event(None, 1000, self.print_event_count)

    def update(self):
        for i in self.events:
            i.check()

        self.clock.tick(self.FPS)
        self.tick += 1
        if self.active_view != None:
            self.active_view._update()
            self._screen.blit(self.active_view._surf, (0, 0))
        pygame.display.flip()


    def mainloop(self):
        loginfo("Engine Mainloop started")
        while True:
            self.update()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    raise SystemExit