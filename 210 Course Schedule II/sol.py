"""
In case of loops => impossible
Otherwise, return the topological sort of the array (one of the possible ordering).
O(N + M) time and space
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def build_graph(n, prerequisites):
            graph = [[] for _ in range(n)]
            for course, prereq in prerequisites:
                # prerequisite -> course
                graph[prereq].append(course)
            return graph
        
        def dfs_top_sort(current_node, graph, visited, stack):
            visited[current_node] = -1
            for neighbour in graph[current_node]:
                if visited[neighbour] == -1:
                    return False
                if visited[neighbour] == 0:
                    if not dfs_top_sort(neighbour, graph, visited, stack):
                        return False
            visited[current_node] = 1
            stack.append(current_node)
            return True
        
        def top_sort(graph):
            visited = [0 for _ in graph]
            stack = []
            for node in range(len(graph)):
                if visited[node] == 0:
                    if not dfs_top_sort(node, graph, visited, stack):
                        return []
            return list(reversed(stack))
        
        graph = build_graph(numCourses, prerequisites)
        return top_sort(graph)