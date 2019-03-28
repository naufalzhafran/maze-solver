import maze

if __name__ == "__main__":
    hasvis = []
    solu = []
    t = maze.Maze()
    t.load_file("maze_small.txt")
    t.get_start()
    t.get_finish()
    t.debug()
    t.draw()
    t.solveDFS([],(1,0),hasvis,[],solu)
    t.printSol(solu)
    print(solu)
    
