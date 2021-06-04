"""
(Very hard problem)
Brute force: compute all the pair distances, sort them and get the kth. O(N^2 logN) time, O(N^2) space.

If we sort the input array we can easily detect the solution space, that is [0, max - min] (we get a 0 when the array has duplicates).
If we consider all the pairs sorted, we want to know the first one that has k - 1 other pairs before itself.
Let count(num) a function counting the number of pairs whose value is less or equal than num.
The k-th pair is the first one having count(num) >= K.
How can we use this function? We can count the pairs, for different values of num.
How to choose num? With binary search! We know the search space in which num can be (that is[0, max - min]),
and for each value we can try we scan the array with a sliding window, in order to compute the pairs in order, and counting them.
If the resulting count is lower than K, we have to count pairs having a result greater than the current num,
otherwise if count(num) >= K, we have to move on the left, always considering the middle value in this case (since we may have found count(num) == K, but it may not be the first one).
O(N logN + W logN) time [sorting + searching and counting, W is max - min], O(1) space

"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            middle = (left + right) // 2    # this is the num of count(num)
            count = 0
            i = 0
            # j is the right side of the window, i the left one
            for j in range(n):
                while nums[j] - nums[i] > middle:
                    # if the pair difference is too big, reduce the window
                    i += 1
                count += j - i
            if count < k:
                left = middle + 1
            else:
                right = middle
        return left