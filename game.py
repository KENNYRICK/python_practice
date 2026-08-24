import pygame

from settings import width, height, fps
from froggy import Frog
from vehicle import Vehicle

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (width, height)
        )

        pygame.display.set_caption("Frogger")

        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Frog()
        self.vehicles = [
            Vehicle(100, 400, 10),
            Vehicle(350, 400, 10),
            Vehicle(600, 400, 16),
            Vehicle(200, 300, -10),
            Vehicle(500, 300, -18),
            Vehicle(100, 200, 18),
            Vehicle(400,200, 10),

            
            


        ]

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                  self.running = False
            if event.type == pygame.KEYDOWN:
                 self.player.move(event.key)

    def update(self):

        for vehicle in self.vehicles:
            vehicle.update()
        self.check_collisions()

    def check_collisions(self):

        for vehicle in self.vehicles:
            if self.player.rect.colliderect(vehicle.rect):
                print("crash")
                self.player.restart()

    def draw(self):
        self.screen.fill((50, 50, 50))
        self.player.draw(self.screen)
        for vehicle in self.vehicles:
            vehicle.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(60)

        pygame.quit()