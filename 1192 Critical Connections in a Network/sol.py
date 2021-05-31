"""
We have to find a bridge, that is an edge that in case it is removed causes the resulting graph to be disconnected.
Naive approach: remove one edge at a time, then do a visit and check whether the graph is connected or not.
O(E * (V + E)) time, O(V + E) space.
To discover them, we are going to modify the DFS, that has to tell, for every visited node, if the edge we used to reach that node is the only one that makes possible to reach the node.
In case it is, that edge is a bridge.
We use discrete time to keep track of when we entered a node for the first time. 
Then we visit the node and it's neighbours recursively (except the parent), assigning the current node a time that is the minimum between our current time and the result of the DFS rooted on the neighbour, and if we end up in an already visited node (a node that already has a timing), we try to update our timer with the neighbour's time, if it is smaller.
We have a failure in case the starting time of a node is the same time when its visit ends: this means that the edge [parent, node] is critical.
O(V + E) time and space

"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def build_graph(n, connections):
            graph = [[] for _ in range(n)]
            for start, end in connections:
                graph[start].append(end)
                graph[end].append(start)
            return graph
        
        def discover_bridges(current_node, parent, graph, times, current_time, bridges):
            arrival_time = current_time
            times[current_node] = arrival_time
            for neighbour in graph[current_node]:
                if times[neighbour] == -1:
                    arrival_time = min(arrival_time, discover_bridges(neighbour, current_node, graph, times, current_time + 1, bridges))
                elif neighbour != parent:
                    arrival_time = min(arrival_time, times[neighbour])
            if current_time == arrival_time and parent != -1:
                bridges.append([parent, current_node])
            return arrival_time
        
        graph = build_graph(n, connections)
        bridges = []
        times = [-1 for _ in range(n)]
        discover_bridges(0, -1, graph, times, 0, bridges)
        return bridges
        
        