"""
Directed graph, we have to traverse it using all the edges, and yielding the lexical order (so at every step we should try first the strings with a lower lexical score).
We build the graph as an hashmap, with keys the labels of nodes, and values a binary heap (aka a priority queue) with all the destinations reachable from a given airport.
Then we use a recursive function to build the itinerary in reversed order: we start from the JFK node and we remove the first destination, recursing on it. When we reach a node with no more destinations, we just add the node to the result.
Finally, when all the queue of destination has been added, we add the node itself.
Finally, we return the reversed list of nodes.

O(N + MlogM) time to build the graph, O(M logM) time to create the result, that is O(M logM)
O(N + M) space
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import heapq
        def build_graph(tickets):
            graph = {}
            for start, end in tickets:
                if start not in graph:
                    graph[start] = []
                if end not in graph:
                    graph[end] = []
                heapq.heappush(graph[start], end)
            return graph
        
        def populate_result(current_node, graph, result):
            edges = graph[current_node]
            while edges:
                next_destination = heapq.heappop(edges)
                populate_result(next_destination, graph, result)
            result.append(current_node)
        
        graph = build_graph(tickets)
        result = []
        populate_result('JFK', graph, result)
        return list(reversed(result))
        