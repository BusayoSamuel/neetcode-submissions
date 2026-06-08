class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        curr = 1
        for i in range(len(nums)):
            curr = curr * nums[i]
            prefix[i] = curr

        curr = 1
        for j in range(len(nums)-1, -1, -1):
            curr = curr * nums[j]
            postfix[j] = curr

        res = []
        curr = 1

        for k in range(len(nums)):
            pre = prefix[k-1] if k > 0 else 1
            post = postfix[k+1] if k < len(nums) - 1 else 1

            res.append(pre * post)

        return res


        