class Node_Astar():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.loc = pos

        self.g_val = 0
        self.h_val = 0
        self.f_val = 0	
    def __eq__(self, other):
        return self.loc == other.loc   
                   
class Maze:
	def __init__(self):
		self.maze = [] # maze[baris][kolom] 
		self.mat = [] # maze with int elements
		self.length = int(0) #horizontal
		self.width = int(0) #vertikal
		self.start = () # point (baris,kolom)
		self.finish = () # point (baris,kolom)
	
	def load_file(self, filename):
		f = open(filename).readlines()
		
		self.length = len(f[0])-1
		
		for line in f:
			self.width = self.width + 1
			self.maze.append(list(line))
			
		self.width = self.width
		
		self.mat = [[0 for x in range (self.length)] for y in range (self.width)]
			
	def get_start(self):
		# Scan starting point
		
		for y in range(self.width):
			if self.maze[y][0] == "0" :
				self.start = (int(y),int(0))
				break
				
	def get_finish(self):
		
		# Scan finishing point
		for y in range(self.width):
			if self.maze[y][self.length-1] == "0" :
				self.finish = (int(y),int(self.length-1))
				break
			
	def look(self, coord, direction):
		
		if direction is 0:
			return (self.maze[coord[0]][coord[1] + 1] == '0')
		elif direction is 1:
			return (self.maze[coord[0] + 1][coord[1]]== '0')
		elif direction is 2:
			return (self.maze[coord[0]][coord[1] - 1]== '0')
		elif direction is 3:
			return (self.maze[coord[0] - 1][coord[1]]== '0')
			
	def move(self, coord, direction):
		if direction is 0:
			return (coord[0], coord[1] + 1)
		elif direction is 1:
			return (coord[0] +1 , coord[1])
		elif direction is 2:
			return (coord[0], coord[1] - 1)
		elif direction is 3:
			return (coord[0] - 1, coord[1])		
			
	"""
	DIRECTION:
	0: Up
	1: Right
	2: Down
	3: Left
	"""

	def draw(self) :
	
		for y in range(self.width):
			for x in range(self.length):
				print(self.maze[y][x], end='')
			print()	
						
	def debug(self):
		print(
		"""
		length: %d
		width: %d
		Start : %s
		Finish : %s
		""".replace("	", "") % (self.length, self.width , self.start, self.finish))
	
	def solveDFS(self, track,startpoint,hasvisited,solution,finalsol):
		# not done
		# still infinity loop

		if(startpoint == self.finish):
			print("fi")
			finalsol = solution
		else:

			ttrack = track
			ttrack.append(startpoint)
			hasvisited.append(startpoint)
			solution.append(startpoint)
			print(startpoint)
			for i in range(0,4):
				if self.look(startpoint,i) and self.move(startpoint,i) not in hasvisited:
					self.solveDFS(ttrack,self.move(startpoint,i),hasvisited,solution,finalsol)
					solution.pop()

	def printSol(self,solution):
		for sol in solution:
			self.maze[sol[0]][sol[1]] = ' '	
			
			
	def convert(self):
		for y in range(self.width): 
			for x in range(self.length):
				self.mat[y][x] = int(self.maze[y][x])

	
	def heuristic_funtion(self, current) :
		#manhattan distance
		dx, dy = current[0] - self.finish[0], current[1] - self.finish[1]
		return abs(dx) + abs(dy)
		
		
	def solve_Astar(self):
		#Return path from end to  finish

		# Initialization
		start_node = Node_Astar(None, self.start)
		start_node.g_val = 0
		start_node.h_val = 0
		start_node.f_val = 0
		end_node = Node_Astar(None, self.finish)
		end_node.g_val = 0
		end_node.h_val = 0
		end_node.f_val = 0
		simpul_hidup = []
		simpul_ekspand = []

		simpul_hidup.append(start_node)

		while len(simpul_hidup) > 0:

			node = simpul_hidup[0]
			index = 0
			for i, n in enumerate(simpul_hidup):
				if n.f_val < node.f_val:
					node = n
					index = i
								
			# Pop 
			simpul_hidup.pop(index)
			simpul_ekspand.append(node)

			# reach goal
			if node == end_node:
				path = []
				current = node
				while current is not None:
					path.append(current.loc)
					current = current.parent
				return path[::-1] 

			# Generate branch
			branch = []
			for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

				# Get node position
				node_position = (node.loc[0] + direction[0], node.loc[1] + direction[1])
				
				new_node = Node_Astar(node, node_position)
				
				if node_position[0] > (len(self.mat) - 1) or node_position[0] < 0 or node_position[1] > (len(self.mat[len(self.mat)-1]) -1) or node_position[1] < 0:
					continue

				if self.mat[node_position[0]][node_position[1]] != 0 or new_node in simpul_ekspand or new_node in simpul_hidup:
					continue

				branch.append(new_node)

			for n in branch:
				# f, g, h val
				n.g_val = node.g_val + 1
				n.h_val = abs((n.loc[0] - end_node.loc[0])) + abs((n.loc[1] - end_node.loc[1]))
				n.f_val = n.g_val + n.h_val

				# Add
				simpul_hidup.append(n)

'''		
#Implementation	
if __name__ == '__main__':
	m = Maze()
	m.load_file("maze_large.txt")
	m.get_start()
	m.get_finish()
	m.convert()
	m.debug()
	m.draw()
	print("langkah :")
	langkah = m.solve_Astar()
	
	print(langkah)


'''
		
