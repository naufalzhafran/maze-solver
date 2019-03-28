class Maze:
	def __init__(self):
		self.maze = [] # maze[baris][kolom] 
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
			
	def get_start(self):
		# Scan starting point
		
		for y in range(self.width):
			if self.maze[y][0] == "0" :
				self.start = (y,0)
				break
				
	def get_finish(self):
		
		# Scan finishing point
		for y in range(self.width):
			if self.maze[y][self.length-1] == "0" :
				self.finish = (y,self.length)
				break
	
	def move(self, coord, direction):
		if direction is 0:
			return (coord[0], coord[1] + 1)
		elif direction is 1:
			return (coord[0] +1 , coord[1])
		elif direction is 2:
			return (coord[0], coord[1] - 1)
		elif direction is 3:
			return (coord[0] - 1, coord[1])
			
	def look(self, coord, direction):
		
		if direction is 0:
			return (self.maze[coord[0]][coord[1] + 1] == '0')
		elif direction is 1:
			return (self.maze[coord[0] + 1][coord[1]]== '0')
		elif direction is 2:
			return (self.maze[coord[0]][coord[1] - 1]== '0')
		elif direction is 3:
			return (self.maze[coord[0] - 1][coord[1]]== '0')
			
	"""
	DIRECTION:
	0: Up
	1: Right
	2: Down
	3: Left
	"""

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
	
	
	def draw(self) :
	
		for y in range(self.width):
			for x in range(self.length):
				print(self.maze[y][x], end ='')
			print()
				
				
				
	def debug(self):
		print(
		"""
		length: %d
		width: %d
		Start : %s
		Finish : %s
		""".replace("	", "") % (self.length, self.width , self.start, self.finish))
		
		

