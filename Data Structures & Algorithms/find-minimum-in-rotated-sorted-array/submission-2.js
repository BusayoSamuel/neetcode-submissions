class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        var l = 0
        var r = nums.length - 1
        var res = nums[0]

        while(l <= r){
            if(nums[l] <= nums[r]){
                return Math.min(res, nums[l])
            }

            var m = Math.floor((r+l)/2)
            res = Math.min(nums[m], res)
            if(nums[m] >= nums[l]){
                l = m + 1
            }else{
                r = m - 1
            }
        }
        return res   
    }
}
