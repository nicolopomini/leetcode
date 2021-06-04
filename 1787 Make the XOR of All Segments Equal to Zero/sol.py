"""
If a group of k elements xor to 0, it means that if we consider only the first k - 1 elements, the element before them must be equal to the last of the first group
For example: 7,3,4 xor to 0. If we take only 7,3, we need a 4 before 7 to make a xor.
Too hard for me, taken from https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/discuss/1099112/C%2B%2B-An-easy-solution-with-detailed-explanation-to-a-really-hard-problem
Let changes[i][j] the minimum number of items in nums[i:] to be changed, in order that the xor of elements of nums[:i] is equal to j. The answer is in changes[0][0].
At index i, we need to select some number such that x ^ {some xor of subarray starting before i} = j, therefore {some xor of subarray starting after i} = x ^ j.
Changes[i][j] is computed summing two things:
- the number of changes to be done at i + 1 to obtain x ^ j, that is changes[i - 1][x ^ j]
- the changes to be done at index i, that are equal to the number of times that index i occurs minus the frequency of x at index i.
Since the values of the array are between 0 and 1024, we can choose x in that range
But:
- we can select an item x such that its frequency at index i is 0, so that the second component is equal everywhere, and in this case the answer is just the min of changes[i - 1]
- we can select an item x whose frequency at i is > 0, and in this case we have to try them all.

"""
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        frequences = [[0 for _ in range(1024)] for _ in range(k)]   # the frequ of each number at each position
        changes = [[n + 1 for _ in range(1024)] for _ in range(k)]  # memory used to dp
        nums_at_pos = [set() for _ in range(k)]                     # set of numbers for every position in the array
        
        for i in range(n):
            # fill the two variables
            position = i % k
            nums_at_pos[position].add(nums[i])
            frequences[position][nums[i]] += 1
        
        best_up_to_last = 0
        for i in range(k):
            # how many positions i we have in the array?
            count_of_pos = n // k + (1 if n % k > i else 0)
            # min number of changes at i
            best_at_i = n + 1
            for j in range(1024):
                if i == 0:
                    # base case: just the number of times we have a position 0, minus the frequence of the current number in that position
                    changes[i][j] = count_of_pos - frequences[i][j]
                else:
                    # try all the numbers occurring at position i
                    for x in nums_at_pos[i]:
                        changes[i][j] = min(changes[i][j], changes[i - 1][x ^ j] + count_of_pos - frequences[i][x])
                    
                    # try all the numbers not occurring at index i
                    changes[i][j] = min(changes[i][j], best_up_to_last + count_of_pos)
                best_at_i = min(best_at_i, changes[i][j])
            best_up_to_last = best_at_i
        
        return changes[k - 1][0]
        