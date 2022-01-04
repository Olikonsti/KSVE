import pymunk
import pygame
from KSVE.UTILS.logger import *

class Entity():
    def __init__(self, view, image, start_pos=(10, 10), fixed=True, width=100, height=100):
        self.view = view

        self.x = start_pos[0]
        self.y = start_pos[1]

        self.width = width
        self.height = height

        self.layer = 0

        self.screenx = 0
        self.screeny = 0

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # ADVANCED PHYSICS
        self.fixed = fixed

        self.shape = pymunk.Poly.create_box(None, size=(self.width, self.height))
        if fixed:
            self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        else:
            self.body = pymunk.Body()
        self.shape.body = self.body
        self.body.position = (self.x, self.y)
        self.view.phy_space.add(self.body, self.shape)
        if not fixed:
            self.poly_m = pymunk.moment_for_poly(1, self.shape.get_vertices())

        # ADVANCED PHYSICS OPTIONS
        self.shape.density = 3
        self.shape.friction = 2

        self.view.entities.append(self)
        loginfo("Entity created")



    def _update(self):
        self.update()
        if not self.fixed:
            self.draw_advanced_physics(self.view._surf)
        else:
            self.draw(self.view._surf)

    def update(self):
        pass

    def draw(self, surf):
        surf.blit(self.image, (self.x-self.width/2, self.y-self.height/2, self.width, self.height))

    def draw_advanced_physics(self, surf):
        draw_bb = False
        points = []
        for v in self.shape.get_vertices():
            x, y = v.rotated(self.shape.body.angle) + self.shape.body.position
            points.append((int(x), int(y)))

        def centroid(vertexes):
            _x_list = [vertex[0] for vertex in vertexes]
            _y_list = [vertex[1] for vertex in vertexes]
            _len = len(vertexes)
            _x = sum(_x_list) / _len
            _y = sum(_y_list) / _len
            return (int(_x), int(_y))

        rotated_image = pygame.transform.rotate(self.image, self.shape.body.angle*-57)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=centroid(points)).topleft)
        surf.blit(rotated_image, new_rect)
        if draw_bb:
            for i in range(3):
                pygame.draw.line(surf, pygame.Color("blue"), points[i], points[i+1])
            pygame.draw.line(surf, pygame.Color("blue"), points[3], points[0])
