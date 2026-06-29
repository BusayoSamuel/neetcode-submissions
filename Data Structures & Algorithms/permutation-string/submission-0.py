class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        s2Count = {}

        l = 0

        for r in range(len(s2)):
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1

            while l <= r and r - l + 1 > len(s1):
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    del s2Count[s2[l]]
                l += 1


            if s1Count == s2Count:
                return True

        return False



