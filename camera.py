import data as data
import pygame


class Camera:
    def __init__(self):
        self.angle = 90
        self.horizontal_angle = 0
        self.position = [300, 300, -100]
        self.speed = 0.8
        self.FOV = 90
        self.focal_length = 70

    def fix_angles(self):
        if self.angle > 180:
            self.angle %= 360
        elif self.angle < -180:
            self.angle %= -360

    def react(self):
        keys = pygame.key.get_pressed()
        actual_speed = self.speed
        if keys[pygame.K_LCTRL]:
            actual_speed *= 5
        elif keys[pygame.K_LSHIFT]:
            actual_speed /= 5
        if keys[pygame.K_UP]:
            self.angle += actual_speed
        elif keys[pygame.K_DOWN]:
            self.angle -= actual_speed
        if keys[pygame.K_LEFT]:
            self.horizontal_angle += actual_speed
        elif keys[pygame.K_RIGHT]:
            self.horizontal_angle -= actual_speed
        # self.fix_angles()