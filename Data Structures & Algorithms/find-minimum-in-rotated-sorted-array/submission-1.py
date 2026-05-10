class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = math.inf

        while l <= r:
            m = (r + l) // 2

            if nums[m] >= nums[l] >= nums[r]:
                l = m + 1
            elif nums[l] <= nums[m] <= nums[r]:
                r = m - 1
            elif nums[m] <= nums[r] <= nums[l]:
                l += 1
            
            res = min(res, nums[m])

        return res
            
            
        