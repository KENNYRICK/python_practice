import pygame

 # pulls data from settings that makes a frog a frog.....aka
from settings import(width, height, green, frog_height, frog_width, frog_start_x, frog_start_y, frog_movement_speed_DND)

class Frog: 
    
    # creates frog rectangle through the constructor self. which data came from settings
    def __init__(self):
        self.x = frog_start_x
        self.y = frog_start_y
        self.width = frog_width
        self.height = frog_height
            
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height

        )

    # froggy move because of...........DABUTON!!!!
    def move(self, DaButon):
        if DaButon == pygame.K_UP:
            self.rect.y -= frog_movement_speed_DND
        elif DaButon == pygame.K_DOWN:
            self.rect.y += frog_movement_speed_DND
        elif DaButon == pygame.K_LEFT:
            self.rect.x -= frog_movement_speed_DND
        elif DaButon == pygame.K_RIGHT:
            self.rect.x += frog_movement_speed_DND
        # method made below to stop froggy from escaping the frame
        self.keep_on_field()

    # method to keep froggy in the game
    def keep_on_field(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
            
    #you died
    def restart(self):
        self.rect.x = self.x
        self.rect.y = self.y

    #make froggy picture
    def draw(self,screen):
        pygame.draw.rect(
            screen,
            green,
            self.rect
        )

