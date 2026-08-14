class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            pos = ord(char) - ord("a")
            if node.children[pos] == None:
                node.children[pos] = TrieNode()
            node = node.children[pos]
        node.word = True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if node.children[pos] == None:
                return False
            node = node.children[pos]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            pos = ord(char) - ord('a')
            if node.children[pos] == None:
                return False
            node = node.children[pos]
        return True
        