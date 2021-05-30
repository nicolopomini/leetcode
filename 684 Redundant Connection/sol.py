"""
We can build the tree incrementally, using a merge-find set.
At the beginning, all the nodes are into an individual set (they are not connected with any other node).
Then we scan the edge list, and we connect two components if the two nodes at the extreme of the edges are not already part of the same component. To detect this fact, we check if the two nodes have different parent nodes in the merge-find set. If this is the case, we merge them, otherwise we found the answer to the problem.

How to implement MFset? A dictionary where all the items are mapped to their parent, and at the beginning every node is its own parent.
Find: starting from one node, follow the chain of parents until we find a node whose parent is the node itself. That is the parent O(N)
Merge: merging two nodes. Find the two parents, and if they are different, set the parent of the shortest branch to the other node O(N).

Space: O(N), time: O(N) due tue the amortized performances of the MFSet
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        merge_find_set = MFSet(len(edges))
        for node1, node2 in edges:
            if merge_find_set.find(node1) == merge_find_set.find(node2):
                return [node1, node2]
            merge_find_set.merge(node1, node2)

        
class MFSet:
    def __init__(self, n):
        self.parents = {i: i for i in range(1, n + 1)}
    
    def find_with_depth(self, n):
        current = n
        depth = 0
        while self.parents[current] != current:
            current = self.parents[current]
            depth += 1
        return current, depth
        
    def find(self, n):
        parent, _ = self.find_with_depth(n)
        return parent
    
    def merge(self, a, b):
        parent_a, depth_a = self.find_with_depth(a)
        parent_b, depth_b = self.find_with_depth(b)
        if parent_a != parent_b:
            if depth_a < depth_b:
                self.parents[parent_a] = parent_b
            else:
                self.parents[parent_b] = parent_a