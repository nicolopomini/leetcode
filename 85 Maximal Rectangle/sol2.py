"""
Another more efficient approach is using the solution of the problem `Largest Rectangle in Histogram`.
We have to transform the current problem into the other one, and apply its solution.
This problem has multiple instances of the other problem: for every row in the matrix, we create a histogram of that row, summing to the current cell the value of the cell aboove, if the current cell > 0.
At this point we can apply the solution of the other problem on every row of the current matrix, and save the greatest area we find.
Let N be the number of rows and M the number of columns, O(NM) time, O(M) space
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largest_rectangle_in_histogram(pillars):
            # O(M) time and space
            pillars.append(0)
            largest_area = 0
            stack = []
            for i in range(len(pillars)):
                while stack and pillars[stack[-1]] >= pillars[i]:
                    height_index = stack.pop(-1)
                    end_rectangle = -1 if not stack else stack[-1]
                    largest_area = max(largest_area, pillars[height_index] * (i - end_rectangle - 1))
                stack.append(i)
            return largest_area
        
        if not matrix:
            return 0
        # first step, transform the matrix from strings to integers
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = int(matrix[row][col])
        
        # compute the consecutive ones on every row, directly on the input matrix
        for row in range(1, len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] > 0:
                    matrix[row][col] += (matrix[row - 1][col])
        
        area = 0
        for row in range(len(matrix)):
            area = max(area, largest_rectangle_in_histogram(matrix[row]))
        return area