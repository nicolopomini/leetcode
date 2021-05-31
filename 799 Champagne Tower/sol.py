"""
Row i has i + 1 columns (glasses). The glasses at the extremes (indexed with 0 and i) have one glass above them from which they are filled, all the other glasses in the middle (1 until i - 1 included) have two.
To fill row 0, we need 1 pouring.
After two pourings, row 1 will be full at half
After 3 pourings, row 1 will be full
After 4 pourings, glass 2,0 will be 1/4 full, glass 2,1 will be half full (because it has 2 glasses above) and glass 2,2 will be 1/4 full.
After 5 pourings, glass 2,0 will be 1/2, glass 2,1 will be full and 2,2 half.
Now things get interesting, because row 3 starts getting filled when row 2 is not yet completed.
In fact, after 6 pourings 2,0 => 3/4, 2,1 => 1, 2,2 => 3/4, but 3,1 => 1/8 and 3,2 => 1/8.

How many pourings passes through the first glass? Exactly equal to `poured`.
How many pourings passes through the second row first glass. Those of the above one - 1 (because the first one stopped entirely abouve) divided by 2. Same on second row second glass.
Third row? It depends on the second! If some glasses on the second row are full, some champagne has flowed below into the third row.
The key point is that we are simulating everything as if all the pouring happend simultaneosuly, so we don't need to keep into consideration all the above rows when filling the current one.
Since the current row depends only on the row above, we can store only two rows in memory.
For every row that we have filled, we go to fill the row below
O(N^2) time, O(N) space, where N is the number of rows of glasses.
"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = [poured]     # first row gets all the pourings
        for row in range(1, query_row + 1):
            next_row = [0 for _ in range(row + 1)]
            for col in range(row):
                # the current glass can flow into two glasses below
                quantity = (current_row[col] - 1.0) / 2.0
                if quantity > 0.0:
                    next_row[col] += quantity
                    next_row[col + 1] += quantity
            current_row = next_row
        return min(1, current_row[query_glass])
                        