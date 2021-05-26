"""
Fixed the root, split the set of remaining values into two: smaller and greater.
For each item, pick the new root, and divide again the set of numbers into smaller and greater

given a list of numbers and an array for the results:
- pick the root and split the remaining items
- recursively create the subtrees
- if no item remaining, return None
"""
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def create_trees(root, items) -> List[TreeNode]:
            if items:
                left_side = [i for i in items if i < root]
                right_side = [i for i in items if i > root]
                left_children = []
                right_children = []
                for left_root in left_side:
                    left_items = list(left_side)
                    left_items.remove(left_root)
                    left_children.extend(create_trees(left_root, left_items))
                for right_root in right_side:
                    right_items = list(right_side)
                    right_items.remove(right_root)
                    right_children.extend(create_trees(right_root, right_items))
                res = []
                if left_children:
                    for lc in left_children:
                        if right_children:
                            for rc in right_children:
                                res.append(TreeNode(val=root, left=lc, right=rc))
                        else:
                            res.append(TreeNode(val=root, left=lc))
                else:
                    if right_children:
                        for rc in right_children:
                            res.append(TreeNode(val=root, right=rc))
                    else:
                        res.append(TreeNode(val=root))
                return res
            else:
                return [TreeNode(val=root)]
        
        items = [i for i in range(1, n + 1)]
        res = []
        for root in items:
            nodes = list(items)
            nodes.remove(root)
            res.extend(create_trees(root, nodes))
        return res