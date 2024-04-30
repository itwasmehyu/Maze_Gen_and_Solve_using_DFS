import pygame
from Maze import Maze_duplicate

pygame.init()
font = pygame.font.Font(None, 32)
sc = pygame.display.set_mode((1200,600))

input_box = pygame.Rect(500, 280, 140, 32)  
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
generated_maze = False
running = True
start = None
end = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
            if generated_maze and (start is None or end is None):
                x,y = pygame.mouse.get_pos()
                # print(x,y)
                for cell in maze.grid_cells:
                    if (x in range(cell.x * cell.TILE,(cell.x + 1) * cell.TILE)) \
                        and (y in range(cell.y * cell.TILE,(cell.y +1) * cell.TILE)):
                        if start:
                            end = (cell.x,cell.y)
                            cell.draw_inside(sc,'yellow')
                        else:
                            start = (cell.x,cell.y)
                            cell.draw_inside(sc,'green')
                        break
                    
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    m, n = map(int, text.split('x'))
                    maze = Maze_duplicate(1200//m)
                    maze.generate_maze(sc)
                    text = ''
                    generated_maze = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                maze.redraw_maze(sc)
        if start and end:
            maze.tracePath(start,end,maze.maze_map(),maze.grid_cells,sc)
            start = None
            end = None
            
    if not generated_maze:
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        sc.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(sc, color, input_box, 2)

    pygame.display.flip()

