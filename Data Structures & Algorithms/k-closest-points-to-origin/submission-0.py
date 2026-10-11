class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(p, q):
            x1, y1 = p
            x2, y2 = q
            distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
            return distance_squared ** 0.5
        
        heap = []
        origin = [0, 0]
        for point in points:
            distance = euclidean_distance(origin, point)
            heapq.heappush(heap, (distance, point))

        closest = []
        for _ in range(k):
            _, point = heapq.heappop(heap)
            closest.append(point)

        return closest