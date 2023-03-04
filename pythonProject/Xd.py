import pygame  # อิมพอรต์โมดูล
pygame.init()

# สร้างจอ
screen = pygame.display.set_mode([800,600])

# กำหนดลูปการทำงาย
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
