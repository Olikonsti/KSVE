from KSVE.GLOBAL import *
from KSVE.UTILS.logger import *

import pygame
import pymunk


class View():
    def __init__(self):
        self._surf = pygame.Surface((1000, 1000))
        self._surf.fill(pygame.Color("red"))

        self.engine = KSVE_ENGINE_INSTANCE[0]

        self.entities = []
        self.events = []

        # ADVANCED PHYSICS
        self.phy_space = pymunk.Space()
        self.phy_space.gravity = 0, 1000

        self.tick = 0

    def _update(self):
        self.tick += 1
        self.update()
        self._surf.fill(pygame.Color("black"))
        try:
            self.phy_space.step(1/(self.engine.clock.get_fps()))
        except Exception as e:
            logwarning(f"Could not update phy_space for active view: {e}")
        for i in self.entities:
            i._update()

    def update(self):
        pass