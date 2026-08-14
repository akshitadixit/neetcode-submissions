class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if not trie.get(char, None):
                trie[char] = {}
            trie = trie[char]
        trie["_"] = True

    def search(self, word: str) -> bool:
        def dfs(trie, j):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for key, child in trie.items():
                        if key != "_" and dfs(child, i+1):
                            return True
                    return False
                elif word[i] in trie:
                    trie = trie[word[i]]
                else:
                    return False
            return isinstance(trie, dict) and trie.get("_", False)

        return dfs(self.trie, 0)
