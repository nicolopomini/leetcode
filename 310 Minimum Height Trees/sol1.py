"""
The root(s) that minimize the height of the tree must be as central as possible; this means that we can remove the leaves (all the nodes with only one link).
At this point we get another tree, with new leaves and other nodes that have more than one link. Again, remove the leaves.
When to stop? When all the remaining nodes have the same number of links. All of them are going to be valid roots.
Pseudocode:
1. Build the graph as a hashmap of int -> set(int)
2. Scan the graph to see if nodes have not the same number of links
3. While there is at least one node with a minimum number of links, remove it
4. Return the remaining nodes

O(nodes) to build the graph, O(nodes) to see if the graph has leaves, O(nodes) to prune the graph. How many times we prune it? O(nodes) time (there are at least 2 leaves at a time)
O(N^2) time, O(N) space
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def build_graph(edges):
            graph = {}
            for start, end in edges:
                if start not in graph:
                    graph[start] = set()
                if end not in graph:
                    graph[end] = set()
                graph[start].add(end)
                graph[end].add(start)
            return graph
        
        def have_same_number_of_edges(graph):
            min_edges = float('inf')
            for node in graph:
                number_of_edges = len(graph[node])
                if min_edges != float('inf') and number_of_edges != min_edges:
                    return False
                min_edges = min(min_edges, number_of_edges)
            return True
        
        def remove_leaves(graph):
            leaves = set()
            for node in graph:
                if len(graph[node]) == 1:
                    leaves.add(node)
            for leaf in leaves:
                graph.pop(leaf)
            for node in graph:
                graph[node] -= leaves
        
        if not edges:
            return [0]
        graph = build_graph(edges)
        while not have_same_number_of_edges(graph):
            remove_leaves(graph)
        return list(graph.keys())