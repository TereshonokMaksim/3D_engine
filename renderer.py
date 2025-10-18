import math
import pygame
import data as data

def distance(point_1: list[int], point_2: list[int]):
    return sum([(point_1[axis] - point_2[axis]) ** 2 for axis in range(3)]) ** 0.5

class Point:
    def __init__(self, relative_position: list, name: str = ""):
        self.absolute_center = [data.screen_size[0] // 2, 
                                data.screen_size[1] // 2, 400]
        self.position = relative_position
        self.name = name
        self.DEV = True

    def draw(self, surface: pygame.Surface, vertical_angle: int = 0, horizontal_angle: int = 0, rotation: int = 0):
        angles = [math.radians(horizontal_angle),
                  math.radians(vertical_angle),
                  math.radians(rotation)]

        x, y, z = self.position
        # im still unsure how rotation matrixes work, but oh well
        x1 = x * math.cos(angles[0]) - z * math.sin(angles[0])
        z1 = x * math.sin(angles[0]) + z * math.cos(angles[0])
        y1 = y

        # vertical rolllll (angle[1] - controlled by arows)
        y2 = y1 * math.cos(angles[1]) - z1 * math.sin(angles[1])
        z2 = y1 * math.sin(angles[1]) + z1 * math.cos(angles[1])
        x2 = x1

        # rollin'
        x3 = x2 * math.cos(angles[2]) - y2 * math.sin(angles[2])
        y3 = x2 * math.sin(angles[2]) + y2 * math.cos(angles[2])
        z3 = z2

        x_offset = x3
        y_offset = y3
        z_offset = z3

        calculated_pos = [self.absolute_center[0] + x_offset, 
                          self.absolute_center[1] + y_offset, 
                          self.absolute_center[2] + z_offset]
        dist = distance(point_1 = calculated_pos,
                        point_2 = data.camera.position)
        visual_multiplier = (data.camera.focal_length / dist) ** (1/3)
        visual_pos = [self.absolute_center[0] + x_offset * 1, 
                      self.absolute_center[1] + y_offset * 1, ]
        
        pygame.draw.circle(surface, (220, 220, 220), visual_pos, max(min(50 * visual_multiplier, 2), 1))

        return [visual_pos, calculated_pos[2], visual_multiplier]

class Cube:
    def __init__(self):
        self.points = [Point([-100, -100,  100], "Point 1"),
                       Point([100,  -100,  100], "Point 2"),
                       Point([100,   100,  100], "Point 3"),
                       Point([-100,  100,  100], "Point 4")]
        self.points2 =[Point([-100, -100, -100], "Point 5"),
                       Point([100,  -100, -100], "Point 6"),
                       Point([100,   100, -100], "Point 7"),
                       Point([-100,  100, -100], "Point 8")]
        self.CUBING = True
    
    def draw(self, surface: pygame.Surface, vertical_angle: int = 0, horizontal_angle: int = 0):
        point_cors = []
        point2_cors = []
        if self.CUBING:
            for corner in self.points:
                point_cors.append(corner.draw(surface = surface, vertical_angle = vertical_angle, horizontal_angle = horizontal_angle))
            pygame.draw.polygon(surface, (220, 220, 220), [point_cors[index][0] for index in range(len(point_cors))], 1)
        for corner in self.points2:
            point2_cors.append(corner.draw(surface = surface, vertical_angle = vertical_angle, horizontal_angle = horizontal_angle))
        pygame.draw.polygon(surface, (220, 220, 220), [point2_cors[index][0] for index in range(len(point2_cors))], 1)
        if self.CUBING:
            for point_index in range(4):
                pygame.draw.line(surface, 
                                 (220, 220, 220), 
                                 point_cors[point_index][0], 
                                 point2_cors[point_index][0], 
                                 min(5, 1))
        return [[round(point2_cors[0][2], 4)], 
                [round(point2_cors[1][2], 4)]]