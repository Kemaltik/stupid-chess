import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))

clock = pygame.time.Clock()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("black")  # Fill the display with a solid color
    rect_x_coord = 0
    rect_y_coord = 0
    previous_colour = "white"
    for i in range(8):
        for j in range(8):
            if previous_colour == "white":
                pygame.draw.rect(screen, (255,0,0), pygame.Rect(rect_x_coord, rect_y_coord, 100, 100))
                previous_colour = "red"
            elif previous_colour == "red":
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(rect_x_coord, rect_y_coord, 100, 100))
                previous_colour = "white"
            rect_x_coord += 100
        rect_y_coord += 100
        rect_x_coord = 0
        if previous_colour == "white":
            previous_colour = "red"
        elif previous_colour == "red":
            previous_colour = "white"

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)