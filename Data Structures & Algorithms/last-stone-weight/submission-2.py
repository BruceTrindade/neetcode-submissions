class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-n for n in stones]
        heapq.heapify(stones_heap)

        while len(stones_heap) > 1:
            y_stone = -heapq.heappop(stones_heap)
            x_stone = -heapq.heappop(stones_heap)

            if x_stone == y_stone:
                continue
            if x_stone < y_stone:
                heapq.heappush(stones_heap,(y_stone - x_stone) * -1)

        if not stones_heap:
            return 0

        return -heapq.heappop(stones_heap)