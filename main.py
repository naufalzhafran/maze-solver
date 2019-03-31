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
    print("A star")
    print("langkah :")
    langkah = t.solve_Astar()
    print(langkah)
    print("Langkah BFS :")
    t.bfs(t.start)
