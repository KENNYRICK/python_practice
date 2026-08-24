import pygame

from settings import(red, width, vehicle_height, vehicle_width, vehicle_start_x, vehicle_speed, vehicle_start_y)

class Vehicle:
        def __init__ (self):
                self.rect = pygame.Rect(
                        vehicle_start_x,
                        vehicle_start_y,
                        vehicle_width,
                        vehicle_height
                )
                self.speed = vehicle_speed

        def update(self):
                self.rect.x += self.speed

                #move vehicle back to other side of screen when reaches end
                if self.rect.left > width:
                    self.rect.right = 0

        def draw(self, screen):
               pygame.draw.rect(
                      screen,
                      red,
                      self.rect
               )


