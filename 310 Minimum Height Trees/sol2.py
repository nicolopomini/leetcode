"""
Better approach (but similar).
A tree can have at most 2 nodes that minimize the height of the tree.
We keep an array of every node, with a set of edges representing the neighbours nodes.
We also keep a list of the current leaves, and we remove them from the tree, updating the leaf list.
We continue doing so until the size of the tree is 2 or smaller.
O(nodes) to build the graph, to identify the leaves. Then every node is added and removed from the leaf array at most once, so overall the time complexity is O(nodes)
Space: O(nodes + edges), to build the graph
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def build_graph(n, edges):
            graph = [set() for _ in range(n)]
            for start, end in edges:
                graph[start].add(end)
                graph[end].add(start)
            return graph
        
        def get_initial_leaves(graph):
            leaves = []
            for i in range(len(graph)):
                if len(graph[i]) == 1:
                    leaves.append(i)
            return leaves
        
        if n <= 2:
            return [i for i in range(n)]
        graph = build_graph(n, edges)
        leaves = get_initial_leaves(graph)
        nodes = n
        while nodes > 2:
            nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbour = list(graph[leaf])[0]
                graph[neighbour].remove(leaf)
                if len(graph[neighbour]) == 1:
                    new_leaves.append(neighbour)
            leaves = new_leaves
        return leaves