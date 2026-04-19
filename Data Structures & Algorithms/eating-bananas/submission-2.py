class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcTime(k):
            t = 0
            for pile in piles:
                if pile % k:
                    t += (pile // k) + 1
                else:
                    t += (pile // k)

            return t

        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            m = (r+l)//2

            if calcTime(m) > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1

        return res


        