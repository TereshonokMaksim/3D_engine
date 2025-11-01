import pygame
import data as data
import camera as camera
import renderer as render

pygame.init()
data.screen_size = [600, 600]
# Amount of FPS text updates per 1 second
FPS_text_updates = 2

data.display = pygame.display.set_mode(data.screen_size)
data.draw_surface = pygame.Surface(data.screen_size, pygame.SRCALPHA)
run = True
data.FPS = 100
clock = pygame.time.Clock()

FPS_data = []
FPS_font = pygame.sysfont.SysFont("Arial", 24)
FPS_pos = [10, 10]
FPS_surface = FPS_font.render("Initing...", True, (200, 200, 200))

ticks = -1

data.camera = camera.Camera()
point = render.Cube()

while run:
    ticks += 1
    clock.tick(data.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    data.display.fill((0, 0, 0))
    data.draw_surface.fill((0, 0, 0))

    # code
    FPS_data.append(clock.get_fps())
    if ticks % (data.FPS // FPS_text_updates) == 0:
        FPS_surface = FPS_font.render(f"FPS: {round(clock.get_fps())}, Min FPS/Max FPS: {round(min(FPS_data))}/{round(max(FPS_data))}", 
                                      True, 
                                      (200, 200, 200))
        FPS_data.clear()

    data.camera.react()
    data_smth = point.draw(data.draw_surface, data.camera.vertical_angle, data.camera.horizontal_angle)

    data.display.blit(data.draw_surface, (0, 0))
    data.display.blit(FPS_surface, FPS_pos)
    data.display.blit(FPS_font.render(f"Angle: {round(data.camera.horizontal_angle), round(data.camera.vertical_angle)}; Position: {[round(val) for val in data.camera.position]}", True, (200, 200, 200)), [FPS_pos[0], FPS_pos[1] + FPS_surface.get_height() + 10])

    pygame.display.flip()