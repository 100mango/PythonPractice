#coding=utf-8

#图 adjacency list
class Vertex:

	def __init__(self, key):
		self.id = key
		self.adjacentTo = {}

	def __str__(self):
		return str(self.id) + 'adjacentTo' + str([vertex.id for vertex in self.adjacentTo])

	def addAdjacentVertex(self,vertex,weight = 0):
		self.adjacentTo[vertex] = weight

	def getAdjacencies(self):
		return self.adjacentTo.keys()
	
	def getWeight(self,vertex):
		return self.adjacentTo[vertex]



class Graph:

	def __init__(self):
		self.vertexs = {}
		self.numberOfVertex = 0

	def __contains__(self,vertex):
		if vertex in self.vertexs:
			return True
		else:
			return False

	def __iter__(self):
		return iter(self.vertexs.values())

	def addVertex(self,key):
		self.numberOfVertex = self.numberOfVertex + 1
		newVertex = Vertex(key)
		self.vertexs[key] = newVertex
		return newVertex

	def getVertex(self,vertexKey):
		if vertexKey in self.vertexs:
			return self.vertexs[vertexKey]
		else:
			return None

	def addEdge(self,from_vertex_key,to_vertex_key,weight = 0):
		if from_vertex_key not in self.vertexs:
			self.addVertex(from_vertex_key)
		if to_vertex_key not in self.vertexs:
			self.addVertex(to_vertex_key)
		self.vertexs[from_vertex_key].addAdjacentVertex(self.vertexs[to_vertex_key],weight)


g = Graph()
for i in range(6):
	g.addVertex(i)

print g.vertexs

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
	for w in v.getAdjacencies():
		print("( %s , %s )" % (v.id, w.id))






