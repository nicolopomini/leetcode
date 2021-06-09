"""
The output is the size of the tree list we can pick with the two baskets.
We can only have two different types in our current window.
We can start from the first one, and use a sliding window indicating the portion of the tree list we can pick.
As long as we face two types of fruits, we can keep increasing our window.
When we would be about to add the third type, we must reduce our window until we remove completely a type before increasing again
We keep a hashmap indicating the current window, and the current maximum window we have seen

O(N) time, O(1) space
"""
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maximum_window = 0
        current_window = {}
        left = 0
        for right in range(len(tree)):
            next_fruit = tree[right]
            while len(current_window) == 2 and next_fruit not in current_window:
                # remove the leftmost fruit
                to_remove = tree[left]
                current_window[to_remove] -= 1
                if current_window[to_remove] == 0:
                    current_window.pop(to_remove)
                left += 1
            # add the fruit
            if next_fruit not in current_window:
                current_window[next_fruit] = 0
            current_window[next_fruit] += 1
            maximum_window = max(maximum_window, right - left + 1)
        return maximum_window
        