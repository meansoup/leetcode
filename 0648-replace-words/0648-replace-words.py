class Solution:
    def makeTrie(self, trie, word):
        cur = trie

        for i in range(len(word) - 1):
            c = word[i]
            if c in cur and "END" in cur[c]:
                return
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur[word[-1]] = {"END": True}

    def makeRoot(self, trie, word):
        cur = trie

        result = ""
        for c in word:
            if "END" in cur:
                return result

            if c in cur:
                result += c
                cur = cur[c]
            else:
                return word
        return word
    
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            self.makeTrie(trie, word)

        result = ""
        word = ""

        for i in range(len(sentence)):
            c = sentence[i]
            if c == " ":
                result += self.makeRoot(trie, word) + " "
                word = ""
            elif i == len(sentence) - 1:
                word += c
                result += self.makeRoot(trie, word)
            else:
                word += c

        return result