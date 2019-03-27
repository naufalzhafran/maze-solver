import maze

if __name__ == "__main__":
    t = maze.Maze()
    t.load_file("maze_small.txt")
    t.draw()
    t.solveDFS([],(1,0))
