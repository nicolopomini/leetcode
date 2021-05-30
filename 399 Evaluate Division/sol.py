"""
Pairs of variables forming some divisions, like a/b, and their results.
We can create a weighted graph, where nodes are variables, and edges connect two variables that are in an equation, and their weight is the result of the division.
If 'a' and 'b' are variables, and a/b = 0.5, we will have an edge from a to b with weight 0.5, and an edge from b to a with weight 2.
Once we formed the graph, every query is going to be a path from the numerator to the denominator. If either the numerator or the denominator are not nodes or the graph, or no path exists, return -1, otherwise we return the product on the edges.
Size of the graph:
- if all the variables in the equations are different, we will have O(equations) nodes and edges
- if all the single variables are connected with all the other variables [e.g. we have a/b, a/c, a/d, b/c, b/d, c/d], than the number of edges is O(equations), and the vertices are also O(equations)
So in general, O(equations) time and space to store the graph.
Every query is a visit, so O(equations) each query.
Overall: O(equations * query) time, O(equations) space
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import deque
        
        def build_graph(equations, values):
            graph = {}
            for i in range(len(equations)):
                num, den = equations[i]
                if num not in graph:
                    graph[num] = []
                if den not in graph:
                    graph[den] = []
                graph[num].append([den, values[i]])
                graph[den].append([num, 1.0 / values[i]])
            return graph
        
        def solve_query(num, den, graph):
            if num not in graph or den not in graph:
                return -1
            queue = deque()
            visited = {node: False for node in graph}
            queue.append((num, 1.0))
            visited[num] = True
            while queue:
                node, current_result = queue.popleft()
                for neighbour, weight in graph[node]:
                    if neighbour == den:
                        return current_result * weight
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        queue.append((neighbour, current_result * weight))
            return -1
        
        graph = build_graph(equations, values)
        results = []
        for query in queries:
            num, den = query
            results.append(solve_query(num, den, graph))
        return results
        