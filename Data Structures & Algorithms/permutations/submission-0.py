class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        selected = set()
        cur = []
        res = []

        def dfs():
            nonlocal selected
            nonlocal cur
            nonlocal res

            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(0, len(nums)):
                if i in selected:
                    continue

                cur.append(nums[i])
                selected.add(i)
                dfs()
                cur.pop()
                selected.remove(i)

        dfs()

        return res



        