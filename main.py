import maze
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 

WIDTH = 20
HEIGHT = 20
 

MARGIN = 0
 

if __name__ == "__main__":
    t = maze.Maze()
    t.load_file("maze_large.txt")
    t.get_start()
    t.get_finish()
    t.convert()
    solve = []
    solve = t.maze.copy()
    langkah = t.solve_Astar()

 
    pygame.init()
 

    WINDOW_SIZE = [len(t.maze) *20, len(t.maze[0]*20)]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    

    pygame.display.set_caption("MAZE")

    done = False
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ans = t.bfs(t.start)
                    print(ans)
                    maze.printSol(solve,ans)
                if event.key == pygame.K_LEFT:
                    print(langkah)
                    maze.printSol(solve,langkah)

        for row in range(len(solve)):
            for column in range(len(solve[0])):
                color = WHITE
                if solve[row][column] == '1':
                    color = GREEN
                elif solve[row][column] == ' ':
                    color = RED
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])

        pygame.display.flip()

pygame.quit()

