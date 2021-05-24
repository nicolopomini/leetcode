"""
Intuition: How many permutations starts with array[1]? (len(array) - 1)!
if k <= (len(array) - 1)!, we can place array[1] as first element, and then see what is the kth permutation with n - 1 items
if k > (len(array) - 1)!, I can consider the second item as the first element, decreasing k by (len(array) - 1)! and recomputing.
I can cache the factorial from 0 until len(array) - 1 to make things faster.

O(N) time and space
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def compute_factorials(n):
            # O(N) time and space
            factorials = [1]
            for i in range(1, n):
                factorials.append(factorials[-1] * i)
            return factorials
        
        def compute_kth_permutation(numbers, k, factorials, combination_so_far):
            # O(N) time and space
            if not numbers:
                return "".join(combination_so_far)
            combinations_with_first_element = factorials[len(numbers) - 1]
            start_element = 0
            while k > combinations_with_first_element:
                k -= combinations_with_first_element
                start_element += 1
            first_element = numbers.pop(start_element)
            combination_so_far.append(first_element)
            return compute_kth_permutation(numbers, k, factorials, combination_so_far)
        
        return compute_kth_permutation([str(i) for i in range(1, n + 1)], k, compute_factorials(n), [])