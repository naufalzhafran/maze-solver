import maze

if __name__ == "__main__":
	hasvis = []
	solu = []
	t = maze.Maze()
	t.load_file("maze_med.txt")
	t.get_start()
	t.get_finish()
	t.convert()	
	t.debug()
	t.draw()
	t.solveDFS([],(1,0),hasvis,[],solu)
	t.printSol(solu)
	print(solu)
	print()
	
	print("A star")
	print("langkah :")
	langkah = t.solve_Astar()
	print(langkah)
	panjang = len(langkah)
	#print(panjang)
	print()
	print("langkah dalam peta = ")
	for i in range(panjang) :
		t.maze[int(langkah[i][0])][int(langkah[i][1])] = "x"
	t.draw()
