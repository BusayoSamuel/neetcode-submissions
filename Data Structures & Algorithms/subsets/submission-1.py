class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []

        def dfs(i):

            if i >= len(nums):
                temp = cur.copy()
                res.append(temp)
                return

            cur.append(nums[i])
            dfs(i+1)

            cur.pop()
            dfs(i+1)

        dfs(0)
        return res

                
        