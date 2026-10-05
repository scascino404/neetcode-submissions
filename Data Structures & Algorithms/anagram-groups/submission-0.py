class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_chars_count(s):
            NUM_CHARS = ord('z') - ord('a') + 1
            count = [0] * NUM_CHARS
            for c in s:
                idx = ord(c) - ord('a')
                count[idx] += 1
            return count
        
        seen = defaultdict(lambda: [])
        for s in strs:
            count = get_chars_count(s)
            seen[tuple(count)].append(s)
        return list(seen.values())
