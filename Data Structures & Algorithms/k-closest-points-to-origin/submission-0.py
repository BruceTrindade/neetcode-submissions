class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap =[]

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            points_heap.append([distance, x, y])

        heapq.heapify(points_heap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(points_heap)
            res.append([x, y])
            k -= 1

        return res    