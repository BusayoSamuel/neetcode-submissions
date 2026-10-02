class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []

        def backtrack(start, total):
            nonlocal cur

            if total == target:
                res.append(cur.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                cur.append(nums[i])
                backtrack(i, total + nums[i])

                cur.pop()

        backtrack(0, 0)
        return res
                



        