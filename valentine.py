import pygame

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Valentine's Day Card")
screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font('freesansbold.ttf', 32)
img = pygame.image.load("snas.jpg")


class shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y 
        self.color = color
        
class Heart(shape):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    
    def draw(self, surface):
        left_circle_center = (self.x - 20, self.y)
        right_circle_center = (self.x + 20, self.y)
        triangle_points = [(self.x - 40, self.y + 5),
                           (self.x + 40, self.y + 5),
                           (self.x, self.y + 50)]
        
        pygame.draw.circle(surface, self.color, left_circle_center, 20)
        pygame.draw.circle(surface, self.color, right_circle_center, 20)
        pygame.draw.polygon(surface, self.color, triangle_points)
class flower(shape):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    def draw(self, surface):
        circle_center = (self.x, self.y)
        triangle_points1 = [(self.x - 20, self.y -30),
                           (self.x - 20, self.y),
                           (self.x, self.y)]
        triangle_points2 = [(self.x - 20, self.y),
                           (self.x + 20, self.y),
                           (self.x-5, self.y-30)]
        triangle_points3 = [(self.x - 20, self.y),
                           (self.x + 20, self.y),
                           (self.x+5, self.y-30)]
        triangle_points4 = [(self.x + 20, self.y -30),
                           (self.x + 20, self.y),
                           (self.x, self.y)]
        stem = (self.x-3, self.y, 5, 50)
        pygame.draw.rect(surface, (0, 250, 0), stem)
        pygame.draw.circle(surface, self.color, circle_center, 20)
        pygame.draw.polygon(surface, self.color, triangle_points1)
        pygame.draw.polygon(surface, self.color, triangle_points2)
        pygame.draw.polygon(surface, self.color, triangle_points3)
        pygame.draw.polygon(surface, self.color, triangle_points4)

# Create instances of Heart
heart1 = Heart(200, 200, (250, 0, 0))
heart2 = Heart(400, 200, (250, 0, 0))  # You can ask students to change positions and colors
flower1 = flower(200, 400, (250, 0, 0))

# Draw everything
screen.blit(img, (0, 400))
heart1.draw(screen)
heart2.draw(screen)
flower1.draw(screen)

text1 = font.render('I Love You!', True, (250, 100, 100))
text2 = font.render('Happy Valentines Day', True, (250, 0, 0), (200, 150, 150))
screen.blit(text1, (200, 100))
screen.blit(text2, (400, 300))


pygame.display.flip()
pygame.time.wait(5000)
