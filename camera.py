import data as data
import pygame
from math import radians, cos, sin


class Camera:
    def __init__(self):
        self.vertical_angle = 0
        self.horizontal_angle = 0
        self.position = [300, 300, 0]
        self.distance = 200
        self.center = [0, 0, 0]
        self.speed = 0.8
        self.FOV = 90
        self.focal_length = 70

    def fix_angles(self):
        if self.vertical_angle > 180:
            self.vertical_angle %= 360
        elif self.vertical_angle < -180:
            self.vertical_angle %= -360

    def reposition(self):
        self.position[1] = self.center[1] + sin(radians(self.vertical_angle)) * self.distance
        self.position[0] = self.center[0] + sin(radians(self.horizontal_angle)) * cos(radians(self.vertical_angle)) * self.distance
        self.position[2] = self.center[2] + cos(radians(self.horizontal_angle)) * cos(radians(self.vertical_angle)) * self.distance

    def react(self):
        keys = pygame.key.get_pressed()
        actual_speed = self.speed
        if keys[pygame.K_LCTRL]:
            actual_speed *= 5
        elif keys[pygame.K_LSHIFT]:
            actual_speed /= 5
        if keys[pygame.K_UP]:
            self.vertical_angle += actual_speed
        elif keys[pygame.K_DOWN]:
            self.vertical_angle -= actual_speed
        if keys[pygame.K_LEFT]:
            self.horizontal_angle += actual_speed
        elif keys[pygame.K_RIGHT]:
            self.horizontal_angle -= actual_speed
        self.reposition()