class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        const selected = new Set()
        const res = []
        const cur = []

        function dfs(){
            if(cur.length === nums.length){
                res.push([...cur])
                return
            }

            for(let i = 0; i < nums.length; i++){
                if(selected.has(i)){
                    continue
                }

                cur.push(nums[i])
                selected.add(i)
                dfs()
                cur.pop()
                selected.delete(i)
            }
        }

        dfs()
        return res
    }
}
