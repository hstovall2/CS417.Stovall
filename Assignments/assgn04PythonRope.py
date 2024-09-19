import networkx as nx

class Rope:
    def __init__(self, value=""):
        self.graph = nx.DiGraph()
        self.root = 0
        self.graph.add_node(self.root, value=value, weight=len(value))
    def recalculateWeights(self, node):
        if not self.graph.has_node(node):
            return
        leftChild = next(self.graph.successors(node), None)
        if leftChild is not None:
            self.graph.nodes[node]['weight'] = self.graph.nodes[leftChild]['weight']
        else:
            self.graph.nodes[node]['weight'] = len(self.graph.nodes[node]['value'])
    def index(self, i):
        current = self.root
        while current is not None:
            weight = self.graph.nodes[current]['weight']
            if i < weight:
                current = next(self.graph.successors(current), None)
            else:
                i -= weight
                current = next(self.graph.successors(current), None)
        return self.graph.nodes[current]['value'][i]
    def concat(self, s2):
        newRoot = len(self.graph)
        self.graph.add_node(newRoot, value="", weight=self.graph.nodes[self.root]['weight'])
        self.graph.add_edge(newRoot, self.root)
        self.graph.add_edge(newRoot, s2.root)
        self.root = newRoot
    def split(self, i):
        pass
    def insert(self, i, s):
        pass
    def delete(self, start, length):
        pass
    def subrope(self, i, j):
        pass
