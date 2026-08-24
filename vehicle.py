import pygame

from settings import(red, width, vehicle_height, vehicle_width, vehicle_start_x, vehicle_speed, vehicle_start_y)

class Vehicle:
        def __init__ (
                      self,
                      x = vehicle_start_x,
                      y = vehicle_start_y,
                      speed = vehicle_speed
        ):
                self.rect = pygame.Rect(
                        x,
                        y,
                        vehicle_width,
                        vehicle_height
                )
                self.speed = speed

        def update(self):
                self.rect.x += self.speed

                #moving right
                if self.speed > 0 and self.rect.left > width:
                        self.rect.right = 0
                #moving left
                elif self.speed < 0 and self.rect.right < 0:
                        self.rect.left = width

        def draw(self, screen):
               pygame.draw.rect(
                      screen,
                      red,
                      self.rect
               )


