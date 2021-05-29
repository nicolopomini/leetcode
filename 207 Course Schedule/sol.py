"""
The courses form a graph, indicating the prerequisites that every course have. In our graph, an edge from i to j means that course i must be taken before j (in other words, j is a prerequisite of i)
In order to be able to do all the courses, the graph must have a topological sorting, and therefore must not contain cycles.
For the visit, we use 3 values: 0 -> not visited, 1 -> already visited, -1 -> current in visit

O(N + M) time and space
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def create_graph(n, prerequisites):
            graph = [[] for _ in range(n)]
            for post, pre in prerequisites:
                graph[pre].append(post)
            return graph
        
        def has_loop(current_node, graph, visited):
            visited[current_node] = -1
            for neighbour in graph[current_node]:
                if visited[neighbour] == 0:
                    # not yet visited, let's visit it
                    if has_loop(neighbour, graph, visited):
                        return True
                elif visited[neighbour] == -1:
                    # found loop
                    return True
            visited[current_node] = 1
            return False
        
        graph = create_graph(numCourses, prerequisites)
        visited = [0 for _ in range(numCourses)]
        for node in range(numCourses):
            if visited[node] == 0:
                if has_loop(node, graph, visited):
                    return False
        return True