class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const counts = new Map()

        for(var num of nums){
            if(!counts.has(num)){
                counts.set(num, 0)
            }

            counts.set(num, counts.get(num) + 1)
        }

        const res = []

        const freqs = new Array(nums.length + 1).fill(null).map(() => [])

        for (let [num, count] of counts) {
            freqs[count].push(num)
        }

        for(let i = freqs.length - 1; i > -1; i--){
            if(freqs[i]){
                for(var num of freqs[i]){
                    res.push(num)
                    if (res.length === k){
                        return res
                    }
                }
            }
        }


    }
}
