class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while (s[i] == ' ' or not s[i].isalnum()) and i < j:
                i += 1
            while (s[j] == ' ' or not s[j].isalnum()) and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True