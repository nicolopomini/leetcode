"""
Preorder: put the node, visit left, visit right
Inorder: visit left, put the node, visit right
Preorder gives us the root, but then we need to know where to split the array between left and right. How can we get this piece of information from the inorder?
We have to look for the index of the root in the inorder: everything coming on the left of that index is the left subtree, everything coming after it is the right subtree.
- Pick the first element of the preorder, that is the root
- search the index of the root element in the inorder: all the items coming before are part of the left subtree, all coming after are in the right one
- we separate the preorder and inorder, creating the left and right preorder and inorder
- we create the node and we recurse
We use a hashmap to map each value in the inorder to its position, for a fast access.
Every time we place a node we exclude the current root from the inorder hashmap, keeping track of the first and the last item we can use to build the tree.

O(N) time and space
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(preorder, inorder_hashmap, left, right, preorder_index):
            # if there are no elements to construct the tree
            if left > right: 
                return None, preorder_index

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left, preorder_index = array_to_tree(preorder, inorder_hashmap, left, inorder_index_map[root_value] - 1, preorder_index)
            root.right, preorder_index = array_to_tree(preorder, inorder_hashmap, inorder_index_map[root_value] + 1, right, preorder_index)

            return root, preorder_index

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        root, _ = array_to_tree(preorder, inorder_index_map, 0, len(preorder) - 1, 0)
        return root