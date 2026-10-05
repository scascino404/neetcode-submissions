class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [(num, count) for num, count in Counter(nums).items()]
        counts.sort(key=lambda t: t[1], reverse=True)
        return [t[0] for t in counts[:k]]