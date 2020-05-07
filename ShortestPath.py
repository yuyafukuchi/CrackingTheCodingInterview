from heapq import heappop,heappush

class Dijkstra():
    def __init__(self,adj_list,startnode):
        self.V = len(adj_list)
        self.startnode = startnode
        self.adj_list = adj_list

        self.mincost = [float('inf')]*self.V
        self.mincost[startnode] = 0
        self.prev = [None]*self.V

        self.queue = [(0,startnode)] #(min_distance,node)

        while self.queue:
            cost,node = heappop(self.queue)
            if self.mincost[node] < cost:
                continue

            for nextnode,weight in self.adj_list[node]:
                if self.mincost[nextnode] > cost + weight:
                    self.mincost[nextnode] = cost + weight
                    self.prev[nextnode] = node
                    heappush(self.queue,(cost + weight,nextnode))

        return

    def get_min(self,G):
        return self.mincost[G]

    def get_min_path(self,G):
        node = G
        path = []
        while node:
            path.append(node)
            node = self.prev[node]
        path.append(self.startnode)
        return path[::-1]


adj = [[(1,5),(2,4),(3,2)],[(0,5),(2,2),(5,6)],[(0,4),(1,2),(3,3),(4,2)],[(0,2),(2,3),(4,6)],[(2,2),(3,6),(5,4)],[(1,6),(4,4)]]
startnode = 0
D = Dijkstra(adj,startnode)
print(D.get_min_path(5))


def warshall_floyd(matrix,V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                matrix[i][j] = min(amtrix[i][j],matrix[i][k]+matrix[k][j])




