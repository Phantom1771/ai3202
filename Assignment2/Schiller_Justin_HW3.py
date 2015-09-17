from sys import argv
import math
script, world, Heuristic = argv

class Node():
	__location=None
	__distFromStart=None
	__heuristicDist=None
	__totalDist=None
	__parent=None
	def __init__ (self):
		self.location=[]
		self.distFromStart=None
		self.heuristicDist=None
		self.totalDist=None
		self.parent=None
	def findAdjacents(self,heur,matrix,visited,opened):
		xDim=len(matrix)
		yDim=len(matrix[:][1])
		xLoc=self.location[0]
		yLoc=self.location[1]
		adjacentNodes=[]
		for i in range(-1,2):
			if(0<=(xLoc+i)<xDim):	
				for j in range(-1,2):
					if(0<=(yLoc+j)<yDim):
						temp=matrix[xLoc+i][yLoc+j]
						blah=[]
						blah.append(xLoc+i)
						blah.append(yLoc+j)
						existing=False
						alreadyOpen=False
						for nodes in visited:
							if blah[0]==nodes[0] and blah[1]==nodes[1]:
								existing=True
						for nodes in opened:
							if blah[0]==nodes.location[0] and blah[1]==nodes.location[1]:
								alreadyOpen=True
						if((existing==False) and (temp != "2")):
							node=Node()
							node.location.append(xLoc+i)
							node.location.append(yLoc+j)
							node.heuristicDist=node.heuristic(heur,xDim,0)
							node.parent=self
							if((abs(i)+abs(j))<2):
								if(temp=="1"):
									node.distFromStart=20+self.distFromStart
								else:
									node.distFromStart=10+self.distFromStart
							else:
								if(temp=="1"):
									node.distFromStart=24 + self.distFromStart
								else:
									node.distFromStart=14 + self.distFromStart
							node.totalDist=(node.heuristicDist + node.distFromStart)
							if(node.location != self.location and alreadyOpen==False):
								adjacentNodes.append(node)
		return adjacentNodes
							
	def heuristic(self,heuristic,destX,destY):
		currentX=self.location[0]
		currentY=self.location[1]
		if (heuristic == "manhattan"):
			return (10*(abs(destX-currentX)+abs(destY-currentY)))
		elif (heuristic == "euclidian"):
			return (10 * math.sqrt(((destX-currentX)**2)+((destY-currentY)**2)))
		else:
			print("Invalid Heuristic")

def findPath(world, Heuristic):
	numLocations=1
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
					matrix[row][column]=item
					column=column + 1
			row = row+1
			maxcolumn=column	
	goalY=row
	goalX=0
	visitedNodes=[]
	openNodes=[]
	node=Node()
	node.location.append(7)
	node.location.append(0)
	node.heuristicDist=node.heuristic(Heuristic,row,0)
	node.distFromStart=0
	node.totalDist=node.heuristicDist
	node.parent=None
	openNodes.append(node)
	finalDistance=0
	nodePath=[]
	goal=False
	while(len(openNodes)!=0) and goal==False:
		closestNode=None
		for nodes in openNodes:
			if closestNode == None:
				closestNode= nodes
			else:
				if(closestNode.totalDist > nodes.totalDist):
					closestNode=nodes	
		adj=closestNode.findAdjacents(Heuristic,matrix, visitedNodes,openNodes)
		numLocations=numLocations+1
		visitedNodes.append(closestNode.location)
		openNodes.remove(closestNode)
		for nodes in adj:
			if nodes.location[0] == goalX and nodes.location[1]==goalY:
				finalDistance=nodes.distFromStart
				while(nodes.parent != None):
					nodePath.append(nodes.location)
					nodes=nodes.parent
				nodePath.append(nodes.location)
				goal=True
			else:
				openNodes.append(nodes)
	nodePathinOrder=nodePath.reverse
	print("The total distance from start to finish is",finalDistance,"following the path:",nodePath[::-1],"and visiting", numLocations, "locations")
	return
findPath(world,Heuristic)
