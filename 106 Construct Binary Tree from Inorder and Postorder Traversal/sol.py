"""
Inorder: visit left, put the current node, visit right
Postorder: visit left, visit right, put the current node
The postorder gives us the value of the root, while the inorder root helps us finding which element compose the left subtree, and which the right one.
As the previous problem, we map every element of inorder to its index, for a fast access.
We stop adding nodes when the index of the first element we can use of inorder is greater than the index of the last element.

O(N) time and space
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def array_to_tree(postorder, root_index, inorder_positions, left, right):
            if left > right:
                return None, root_index
            root_value = postorder[root_index]
            root_index -= 1
            root = TreeNode(root_value)
            
            root.right, root_index = array_to_tree(postorder, root_index, inorder_positions, inorder_positions[root_value] + 1, right)
            root.left, root_index = array_to_tree(postorder, root_index, inorder_positions, left, inorder_positions[root_value] - 1)
            return root, root_index
        
        def create_value_pos_map(array):
            value_pos = {}
            for i in range(len(array)):
                value_pos[array[i]] = i
            return value_pos
        
        inorder_position_map = create_value_pos_map(inorder)
        root, _ = array_to_tree(postorder, len(postorder) - 1, inorder_position_map, 0, len(inorder) - 1)
        return root