"""
Greedy approach: scan all the stations, storing their fuel capacity into a max heap.
By the time we travel a distance that requires more fuel than what we have in the tank, we pick the station that allows us to travel the farthest, increasing the current fuel and the number of stops we made.
If we run out of stations and the current distance is not yet greater or equal than the target, we cannot reach it.
At every step we travel ahead (and we consume) a distance that is equal to the current position - the previous position.
O(N logN) time, O(N) space
"""
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        import heapq
        gas_amounts = []
        stops = 0
        travelled_distance = 0
        current_fuel = startFuel
        previous_station = 0
        stations.append([target, float('inf')])
        for distance, fuel in stations:
            current_fuel -= distance - previous_station
            while current_fuel < 0 and len(gas_amounts) > 0:
                current_fuel -= heapq.heappop(gas_amounts)
                stops += 1
            if current_fuel < 0:
                return -1
            heapq.heappush(gas_amounts, -fuel)
            travelled_distance += distance - previous_station
            if travelled_distance >= target:
                return stops
            previous_station = distance
        return stops if travelled_distance >= target else -1