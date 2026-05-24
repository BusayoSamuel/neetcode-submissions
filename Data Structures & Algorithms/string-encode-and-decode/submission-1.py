class Solution:

    def __init__(self):
        self.hashmap = {}
        self.pointer = 0

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(self.pointer)
            self.hashmap[self.pointer] = s
            self.pointer += 1

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(self.pointer):
            res.append(self.hashmap[i])

        return res

