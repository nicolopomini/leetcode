"""
Step 1: organize the input, creating nodes with their colour and a list of edges
Step 2: start visiting the graph from the node 0, with a DFS.
- we have to be ready to detect loops
- we have to keep track of the colors we met so far, and their counters (how many times we saw them)
So, a DSF will start from a non-visited node, and every node will have a hashmap to count the colors seen on its paths
The visit will go as deep as possible, until a node with no neighbours is faced. The colors met by that node are just the color of the node itself.
Then the parent will update its color map with the values of its children. That is, since all the paths passing from the current node can take all the paths from the current node, it is correct to propagate the information backwards.
For every color, we must set the maximum possible obtainable by any path starting from any neighbour
If we detect a loop, we can interrupt the visit, returning some special value indicating that a loop was detected, returning -1.
Since a valid input does not have loops, we must have at least one node without a parent. We must start the visit there: in this way we are sure to consider the longest colored path every time
If no nodes have no parent, it means that there is a loop.
O(V + E) time and space
"""
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def build_graph(colors, edges):
            graph = []
            for i in range(len(colors)):
                node = Node(i)
                node.colors[colors[i]] = 1
                graph.append(node)
            for start, end in edges:
                graph[start].edges.append(end)
                graph[end].in_degree += 1
            return graph
        
        def merge_colors(original_colors, current_colors, neighbour_colors, answer):
            # merges the neighbour colors with the original colors saving them into the current colors, and update the answer
            for color in neighbour_colors:
                if original_colors.get(color, 0) + neighbour_colors[color] > current_colors.get(color, 0):
                    current_colors[color] = original_colors.get(color, 0) + neighbour_colors[color]
                    answer = max(answer, current_colors[color])
            return answer
        
        def dfs(current_node, graph, visited, answer):
            visited[current_node.label] = -1
            # we need to keep track of the original colors of the node, in order to use only the neighbour node that increments one color the most
            original_colors = dict(current_node.colors)
            for neighbour in current_node.edges:
                if visited[neighbour] == -1:
                    return -1
                if visited[neighbour] == 0:
                    neighbour_node = graph[neighbour]
                    answer = dfs(neighbour_node, graph, visited, answer)
                    if answer == -1:
                        return -1
                    # merge the color counters
                    answer = merge_colors(original_colors, current_node.colors, neighbour_node.colors, answer)
                else:
                    # already visited node, I need to merge the counters also here
                    neighbour_node = graph[neighbour]
                    answer = merge_colors(original_colors, current_node.colors, neighbour_node.colors, answer)
            visited[current_node.label] = 1
            return answer
                            
                            
        
        graph = build_graph(colors, edges)
        answer = 1
        visited = [0 for _ in graph]
        parents = [node for node in graph if node.in_degree == 0]
        if not parents:
            return -1
        for node in parents:
            # the visits starts from all the parents
            if visited[node.label] == 0:
                answer = dfs(node, graph, visited, answer)
                if answer == -1:
                    return -1
        for node in graph:
            # if some non-parent node is not already visited, it means that then graph have multiple components, and at list one component is a loop
            if visited[node.label] == 0:
                return -1
        return answer
        
        
        
        
class Node:
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.colors = {}
        self.in_degree = 0