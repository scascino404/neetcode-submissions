class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def get_chars_count(string):
            NUM_CHARS = ord('z') - ord('a') + 1
            count = [0] * NUM_CHARS
            for c in string:
                idx = ord(c) - ord('a')
                count[idx] += 1
            return count

        s_chars_count = get_chars_count(s)
        t_chars_count = get_chars_count(t)
        for sc, tc in zip(s_chars_count, t_chars_count):
            if sc != tc:
                return False
                
        return True