class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)

        # Remove the k largest numbers
        larger = []
        for _ in range(min(self.k, len(self.heap))):
            larger.append(heapq.heappop(self.heap))

        res = -larger[-1]

        # Add the k largest number back
        for num in larger:
            heapq.heappush(self.heap, num)

        return res

