class Solution:
    def encode(self, strs: List[str]) -> str:
        # The input strings have a length up to 200,
        # so 3 digits are enough to encode their length
        encoded_strs = [f"{len(s):03d}{s}" for s in strs]
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            n = int(s[i:i+3])
            i += 3
            strs.append(s[i:i+n])
            i += n
        return strs
