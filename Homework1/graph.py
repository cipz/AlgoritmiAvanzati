
class Graph:

    def __init__(self, lv, le):
        self.Lv = lv
        self.Le = le

    def buildGraph(self, input):
        lines = input.readlines()
        n = lines[0].split()[0]  # Extract number of vertexes
        for i in range(0, int(n)):
            self.Lv.append(Vertex(0, "NULL"))
        lines.pop(0)
        for line in lines:
            info = list(map(int, line.split()))  # Convert all the strings deriving from split to int
            self.Le.append(Edge(info[0] - 1, info[1] - 1, info[2]))

class Vertex:

    def __init__(self, id, p):
        self.ID = id
        self.parent = p


class Edge:

    def __init__(self, u, v, w):
        self.v1 = u
        self.v2 = v
        self.weight = w
        self.label = "NULL"
