"""
Taken from the discussion, too hard for me: https://leetcode.com/problems/redundant-connection-ii/discuss/108058/one-pass-disjoint-set-solution-with-explain
In a nutshell, we can have 3 situations:
1. there is a node with two incoming edges e1 and e2 (with two parents), and the graph has no loops. In this case removing either e1 or e2 solves the problem, we have to remove the last seen one
2. there is a node with two incoming edges e1 and e2, and there is a loop starting at that node and ending with e2. In this case e2 must be removed
3. Every node has only one parent, this means that there is a loop. Any edge could be removed, but since we have to remove the last seen edge, we remove the edge that closes the loop.

The code keeps track of:
- the index of the two edges that arrives on the same node (first and second), the index is relative to the edges array
- the index of the last edges seen in the cycle (last).
- an array of parents, indicating for every node which is its parent
- an array disjoint_set, to find the components of the graph (similarly to the undirected version of the problem).
We scan the edges, and we analyze the various cases:
- if the destination of the current edge has already a parent, it means we have just found the second incoming edge on that node, and we save the two edges
- otherwise, we save the parent of the current node, and we look for the group in which the parent of the current node belongs to: 
- in case it belongs to the same group of the current node (actually, its group is identified exactly by the current node, since we are in a loop), that is the last edge that forms the cycle, and so we save it
- otherwise, we set the group of the current node.

O(N) time and space
"""
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(disjoint_set, index):
            if disjoint_set[index] == 0:
                return index
            disjoint_set[index] = find(disjoint_set, disjoint_set[index])
            return disjoint_set[index]
        
        n = len(edges)
        parent = [-1 for _ in range(n + 1)]
        disjoint_set = [0 for _ in range(n + 1)]
        first = None
        second = None
        last = None
        for i in range(n):
            start, end = edges[i]
            if parent[end] != -1:
                # two incoming edges detected!
                first = parent[end]
                second = i
                continue
            parent[end] = i
            start_group = find(disjoint_set, start)
            if start_group == end:
                last = i
            else:
                disjoint_set[end] = start_group
        if last is None:
            return edges[second]
        if second is None:
            return edges[last]
        return edges[first]