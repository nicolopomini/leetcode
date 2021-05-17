"""
For all the points:
- scan all the other points, and compute the line equation passing through the two points. Slope = (y1 - y2) / (x1 - x2).
- we use the slope to identify one line. Store the slope into a hash table to count how many points share the same slope.
- actually, since the slope is a float, we may run into approximation problems, so we want to store the equation as numerator and denominator, reduced at the minimum terms.
    To do so:
    - compute the gcd between the two numbers;
    - pay attention to negative slopes, being sure to store the negative sign everywhere on the same part (either numerator or denom, otherwise (-1/3) and (1/-3) will be two different keys in the hashmap even though they represent the same line)
    - use the tuple (numerator / gdc, denom / gdc) [as integers] as keys
- reset the hashtable, to make it ready for the next point

O(N^2) time, O(1) space
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def max_points_on_line_passing_by(points, main_index):
            slopes = {}
            max_points = 1
            for i in range(len(points)):
                if i != main_index:
                    numerator = points[main_index][1] - points[i][1]
                    denom = points[main_index][0] - points[i][0]
                    common_divisor = gcd(abs(numerator), abs(denom))
                    numerator /= common_divisor
                    denom /= common_divisor
                    if numerator * denom < 0:
                        numerator = -abs(numerator)
                        denom = abs(denom)
                    key = (int(numerator), int(denom))
                    if key not in slopes:
                        slopes[key] = 1
                    slopes[key] += 1
                    max_points = max(max_points, slopes[key])
            return max_points


        def gcd(a, b):
            if b > a:
                a, b = b, a
            while b != 0:
                a, b = b, a % b
            return a
        
        max_points = 0
        for i in range(len(points)):
            max_points = max(max_points, max_points_on_line_passing_by(points, i))
        return max_points
