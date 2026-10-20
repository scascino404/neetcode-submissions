from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def edit_distance(w1, w2):
            M, N = len(w1), len(w2)

            if M ==  0 or N == 0:
                return abs(M - N)
            
            if w1[0] == w2[0]:
                return edit_distance(w1[1:], w2[1:])
            else:
                return 1 + min(
                    edit_distance(f'{w2[0]}{w1}', w2),     # Insert
                    edit_distance(w1[1:], w2),             # Delete
                    edit_distance(f'{w2[0]}{w1[1:]}', w2)  # Replace
                )
        
        return edit_distance(word1, word2)