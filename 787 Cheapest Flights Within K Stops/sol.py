"""
We need to build a weighted graph, creating an array of n items, where each item is a list of the edges exiting from that node, together with the costs.
Then we need to traverse the graph, doing a BFS: in the queue we push the node, its current cost needed to reach it and the number of steps needed to reach it.
When we pop a node, we store the current size of the queue, because we want to visit all the enqueued nodes before starting with a new round of visit. That is because we may modify the cost or the steps needed to reach some node already in the queue, and therefore we want to visit it before the modifications.
We push into the queue a node if visiting it coming from the current node produces a better path (in terms of cost).
In case the current path would be longer than k steps, we don't push.

Space complexity: the queue has at most N nodes inside of it, and the graph is O(N + M) space
Time complexity: O(N + M) to build it, and every node is added in the queue at most k times, so O(kN)
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import deque
        
        def build_graph(n, flights):
            graph = [[] for _ in range(n)]
            for source, dest, price in flights:
                graph[source].append([dest, price])
            return graph
        
        graph = build_graph(n, flights)
        distances = [float('inf') for _ in range(n)]
        distances[src] = 0
        queue = deque()
        queue.append((src, 0, 0))
        while queue:
            current_size = len(queue)
            while current_size > 0:
                current_size -= 1
                node, steps, cost_so_far = queue.popleft()
                if steps > k:
                    continue
                for neighbour, cost in graph[node]:
                    if distances[neighbour] > cost_so_far + cost:
                        distances[neighbour] = cost_so_far + cost
                        queue.append((neighbour, steps + 1, cost_so_far + cost))
        return distances[dst] if distances[dst] != float('inf') else -1
                
