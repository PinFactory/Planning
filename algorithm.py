import collections

class Graph:
	def __init__(self):
		self.edges = {}

	def neighbors(self, id):
		return self.edges[id]

class Queue:
	def __init__(self):
		self.elements = collections.deque()

	def empty(self):
		return len(self.elements) == 0

	def put( self, x):
		self.elements.append(x)

	def get(self):
		return self.elements.popleft()

def bfs( graph, start ):
	frontier = Queue()
	frontier.put(start)
	visited = {}
	visited[start] = True

	while not frontier.empty():
		current = frontier.get()
		print("Visiting %r" % current)
		for next in graph.neighbors(current):
			if next not in visited:
				frontier.put(next)
				visited[next] = True
				print(visited)




example_graph = Graph()

example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}

print example_graph.neighbors('A')

bfs(example_graph, 'A')

