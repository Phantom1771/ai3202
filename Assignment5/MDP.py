from sys import argv
import math
script, world, E = argv

class Node():
	__xLoc=0
	__yLoc=0
	__Type=None
	__reward=0
	__util=0
	__delta=100
	__parent=None
	def __init__ (self):
		self.xLoc=0
		self.yLoc=0
		self.reward=0.0
		self.util=0.0
		self.delta=100
		self.Type=None
		self.parent=None
def valueIteration(matrix,err):
	xDim=len(matrix)
	yDim=len(matrix[:][1])
	maxdelta=100
	while maxdelta > err:
		maxdelta=0
		for x in range(0,xDim):
			for y in range(yDim-1,-1,-1):
				curUtil=matrix[x][y].util
				if matrix[x][y].reward==50:
					matrix[x][y].util=50
					matrix[x][y].delta=0
				else:
					a1=0
					a2=0
					a3=0
					a4=0
					if(y+1 < yDim and matrix[x][y+1].Type != '2'):
						a1=a1 + 0.8*matrix[x][y+1].util
						a3=a3 + 0.1*matrix[x][y+1].util
						a4=a4 + 0.1*matrix[x][y+1].util
					else:
						a1=a1 - 100000
						if(x+1 < xDim and matrix[x+1][y].Type != '2'):
							a3=a3 + 0.1*matrix[x+1][y].util
						if(x-1 < xDim and matrix[x-1][y].Type != '2'):
							a4=a4 + 0.1*matrix[x-1][y].util
					if(y-1 >=0 and matrix[x][y-1].Type != '2'):
						a2=a2 + 0.8*matrix[x][y-1].util
						a3=a3 + 0.1*matrix[x][y-1].util
						a4=a4 + 0.1*matrix[x][y-1].util
					else:
						a2=a2 - 100000
						if(x+1 < xDim and matrix[x+1][y].Type != '2'):
							a3=a3 + 0.1*matrix[x+1][y].util
						if(x-1 < xDim and matrix[x-1][y].Type != '2'):
							a4=a4 + 0.1*matrix[x-1][y].util
					if(x+1 < xDim and matrix[x+1][y].Type != '2'):
						a3=a3 + 0.8*matrix[x+1][y].util
						a1=a1 + 0.1*matrix[x+1][y].util
						a2=a2 + 0.1*matrix[x+1][y].util
					else:
						a3=a3 - 100000
						if(y+1 < yDim and matrix[x][y+1].Type != '2'):
							a1=a1 + 0.1*matrix[x][y+1].util
						if(y-1 < yDim and matrix[x][y-1].Type != '2'):
							a2=a2 + 0.1*matrix[x][y-1].util
					if(x-1 >=0 and matrix[x-1][y].Type != '2'):
						a4=a4 + 0.8*matrix[x-1][y].util
						a1=a1 + 0.1*matrix[x-1][y].util
						a2=a2 + 0.1*matrix[x-1][y].util
					else:
						a4=a4 - 100000
						if(y+1 < yDim and matrix[x][y+1].Type != '2'):
							a1=a1 + 0.1*matrix[x][y+1].util
						if(y-1 < yDim and matrix[x][y-1].Type != '2'):
							a2=a2 + 0.1*matrix[x][y-1].util
					matrix[x][y].util=(matrix[x][y]).reward + 0.9*max(a1,a2,a3,a4)
					utilPrime=(matrix[x][y]).util
					if(abs(utilPrime - curUtil) < matrix[x][y].delta):
						matrix[x][y].delta = abs(utilPrime - curUtil)
					if matrix[x][y].delta > maxdelta:
						maxdelta=matrix[x][y].delta

def searchUtils(matrix,x,y):
	path=[]
	xDim=len(matrix)
	yDim=len(matrix[:][1])
	path.append("("+str(x)+","+str(y)+")"+", "+str(matrix[x][y].util))
	while(matrix[x][y].reward != 50):
		if(y+1 < yDim and matrix[x][y+1].Type != '2'):
			a1=matrix[x][y+1].util
		else:
			a1=-100000000
		if(y-1 >=0 and matrix[x][y-1].Type != '2'):
			a2=matrix[x][y-1].util
		else:
			a2=-100000000
		if(x+1 < xDim and matrix[x+1][y].Type != '2'):
			a3=matrix[x+1][y].util
		else:
			a3=-100000000
		if(x-1 >=0 and matrix[x-1][y].Type != '2'):
			a4=matrix[x-1][y].util
		else:
			a4=-100000000
		Max=max(a1,a2,a3,a4)
		if Max == a1:
			path.append("("+str(x)+","+str(y+1)+"), "+str(matrix[x][y+1].util))
			matrix[x][y+1].parent=matrix[x][y]
			y=y+1
		elif Max == a2:
			path.append("("+str(x)+","+str(y-1)+"), "+str(matrix[x][y-1].util))
			matrix[x][y-1].parent=matrix[x][y]
			y=y-1
		elif Max == a3:
			path.append("("+str(x+1)+","+str(y)+"), "+str(matrix[x+1][y].util))
			matrix[x+1][y].parent=matrix[x][y]
			x = x + 1
		else:
			path.append("("+str(x-1)+","+str(y)+"), "+str(matrix[x-1][y].util))
			matrix[x-1][y].parent=matrix[x][y]
			x = x - 1
	return path
	
def findPath(world,E):
	matrix=[[0 for i in range(10)] for j in range(8)]
	row=0
	column=0
	with open (world, 'r') as data:
		for line in data:
			line=line.strip()
			items=line.split(" ")
			column=0
			for item in items:
				if column <=9 and row<=7:
					node = Node()
					node.Type=item
					if item == '0':
						node.reward=0
					elif item == '1':
						node.reward = (-1)
					elif item == '2':
						node.reward=-100000000
					elif item == '3':
						node.reward = (-2)
					elif item == '4':
						node.reward = 1
					elif item == '50':
						node.reward = 50
					node.xLoc = column
					node.yLoc = row
					matrix[row][column]=node
					column=column + 1
			row = row+1
			maxcolumn=column
	valueIteration(matrix,(float(E)/9))
	foundPath=searchUtils(matrix,7,0)
	print("The path found is shown as (location),utility " +str(foundPath))
	
def main():
	
	findPath(world,E)

if __name__ == '__main__':
	main()

