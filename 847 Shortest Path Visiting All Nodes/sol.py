"""
We use a BFS, which allows us to discover the shortest path first.
In the BFS queue we put some Path instances. The Path class contains the current node we are at, the visited nodes in the previous section of the path, and the number of visited nodes.
The visited nodes are represented by an integer, where each bit i is 0 if node i is not visited, 1 otherwise. When all the bits of the available nodes are at 1, it means we found a path.
In order to avoid enqueuing duplicated paths, we define the hash method in the Path class (using only the current node and the visited mask) and we keep a set of paths.
"""
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        
        from collections import deque
        queue = deque()
        paths = set()
        for i in range(len(graph)):
            path = Path(i, 1 << i, 0)
            queue.append(path)
            paths.add(path)
        while queue:
            path = queue.popleft()
            for neighbour in graph[path.current_node]:
                mask = path.visited | 1 << neighbour
                if mask == (1 << len(graph)) - 1:
                    return path.cost + 1
                new_path = Path(neighbour, mask, 1 + path.cost)
                if new_path not in paths:
                    paths.add(new_path)
                    queue.append(new_path)
        return -1

        
class Path:
    def __init__(self, current_node, visited, cost):
        self.current_node = current_node
        self.visited = visited
        self.cost = cost
    
    def __eq__(self, o):
        return self.current_node == o.current_node and self.visited == o.visited
    
    def __hash__(self):
        return hash((self.current_node, self.visited))