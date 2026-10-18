class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while stack:
            current, idx = stack.pop()
            if idx >= len(word):
                if current.is_end:
                    return True
                else:
                    continue
            char = word[idx]
            if char != '.':
                if char in current.children:
                    stack.append((current.children[char], idx+1))
            else:
                for child in current.children.values():
                    stack.append((child, idx+1))
        return False
