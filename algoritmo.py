class outputs:
    def __init__(self):
        self.route = []
        self.Routes = []
        self.listaBuses = ["P6", "P13", "RD"]
    
    def updateRoute(self, addition):
        self.route.append(addition)
    
    def updateRoutes(self):
        self.Routes.append(self.route)

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.level = -1
        self.adjacent = []
        self.buses = []
        self.save = []

    def addAdjacent(self, v):
        if v not in self.adjacent:
            self.adjacent.append(v)

class Grafica:
    def __init__(self):
        self.nodes = {}
    
    def addNode(self, v):
        if v not in self.nodes:
            self.nodes[v] = Node(v)

    def addLine(self, a, b):
        if a in self.nodes and b in self.nodes:
            self.nodes[a].addAdjacent(b)
            self.nodes[b].addAdjacent(a)

    def unVisitNodes(self, inicio):
        for node in self.nodes:
            if (self.nodes[node].name == inicio.name):
                continue
            self.nodes[node].visited = False

    def reVisit(self, list):
        for station in list:
            if (station in self.nodes):
                self.nodes[station].visited = True

grafo = Grafica()
out = outputs()

# def ir(inicio, fin):
#     for bus in out.listaBuses:
#         # out.route = []
#         start = grafo.nodes[inicio]
#         start.visited = True
#         if (bus in start.buses):
#             # addToRoute(start.name)
#             # addToRoute(bus)
#             look(start,bus,fin, inicio)

# def look(node, bus, end, inicio):
#     for nod in node.adjacent:
#         # grafo.nodes[node].visited = True
#         node.visited = True
#         if (out.route == []):
#             addToRoute(node.name)
#         n = grafo.nodes[nod]
#         if (n.visited):
#             continue 
#         else:
#             if (bus in n.buses):
#                 addToRoute(bus)
#                 addToRoute(n.name)
#                 n.visited = True
#                 if (n.name == end):
#                     out.updateRoutes()
#                     grafo.unVisitNodes(inicio) #Modify to not unvisit A
#                     out.route = [inicio]
#                     continue
#                 look(n, bus, end, inicio)

def ir(inicio, fin):
    # out.route = []
    start = grafo.nodes[inicio]
    start.visited = True
    look(start, fin, start)


def look(node, end, inicio):
    moved = False
    reachedEnd = False
    for bus in node.buses:
        for nod in node.adjacent:
            # grafo.nodes[node].visited = True
            node.visited = True
            if (out.route == []):
                addToRoute(node.name)
                moved = True
            n = grafo.nodes[nod]
            if (n.visited):
                continue 
            else:
                if (bus in n.buses):
                    addToRoute(bus)
                    addToRoute(n.name)
                    n.save = out.route.copy()
                    moved = True
                    n.visited = True
                    if (n.name == end):
                        reachedEnd = True
                        out.updateRoutes()
                        grafo.unVisitNodes(inicio) #Modify to not unvisit INICIO FROM ir()
                        out.route = node.save.copy()
                        grafo.reVisit(out.route)
                        continue
                        # break
                        # return
                    look(n, end, inicio)
                    out.route = node.save.copy()
                    grafo.unVisitNodes(inicio)
                    grafo.reVisit(out.route)
    # if (moved == False and reachedEnd == False and len(out.route) > 2):
    #     out.route.pop()
    #     out.route.pop()


def addToRoute(node):
    out.updateRoute(node)

def main():
    estaciones = ["A", "B", "C", "D"]
    
    for i in estaciones:
        grafo.addNode(i)
    
    grafo.nodes["A"].buses = ["P6", "RD"]
    grafo.nodes["B"].buses = ["P6", "P3", "P13", "RD", "P8"]
    grafo.nodes["C"].buses = ["P3","RD"]
    grafo.nodes["D"].buses = ["P8", "P6", "P3"]
    lista = ["A","B","A","C","A","D","B","A","B","C","B","D","C","A","C","B","D","A","D","B"]
    # lista = ["A","B","A","C","B","A","B","C","B","D","C","A","C","B","D","B"]

    for n in range(0, len(lista)-1, 2):
        grafo.addLine(lista[n], lista[n+1])

    for i in grafo.nodes:
        print(i, grafo.nodes[i].adjacent)

    ir("C","A")  #Con A -> D faltan 3 resultados (de C a B con RD)
    for element in out.Routes:
        print(element)

main()