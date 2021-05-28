"""
Using dynamic programming.
Let max_distance[i] the maximum distance reachable with i stops.
max_distance[0] is clearly equal to startFuel.
To define all the other items, we have to scan the stations in order: if I entered station i with x fuel, I can now travel x + gas_i with one more stop.
So we go back in the max_distance array, looking for all the distances that can reach the current station with s steps, and updating the s + 1 position using the current station.
O(N^2) time, O(N) space
"""
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_distance = [0 for _ in range(len(stations) + 1)]
        max_distance[0] = startFuel
        for i in range(len(stations)):
            distance, fuel = stations[i]
            for steps in range(i, -1, -1):
                if max_distance[steps] >= distance:
                    max_distance[steps + 1] = max(max_distance[steps + 1], max_distance[steps] + fuel)
        
        # search for the minimum number of steps needed to reach the end
        for i in range(len(max_distance)):
            if max_distance[i] >= target:
                return i
        return -1