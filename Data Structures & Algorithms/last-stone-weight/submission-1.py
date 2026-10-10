class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # All the negations in this function allow to
        # use heapq's max heap as a min heap.
        for i, stone in enumerate(stones):
            stones[i] = -stone
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, -(y - x))
        return -stones[0] if stones else 0