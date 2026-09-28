class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def searchRoot(word, root):
            curr = root
            for i, c in enumerate(word):
                if c not in curr.children:
                    if c == '.':
                        for char in curr.children:
                            if searchRoot(word[i+1:], curr.children[char]):
                                return True
                    return False
                curr = curr.children[c]
            return curr.word

        return searchRoot(word, self.root)
