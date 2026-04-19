class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = Counter(s)

        for c in t:
            if c in scount:
                scount[c] -= 1
                if not scount[c]:
                    del scount[c]
            else:
                return False

        return not scount or min(scount.values()) == max(scount.values()) == 0
        