class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        var l = 0;
        var res = 0;

        for(let r = 0; r < prices.length; r++){
            res = Math.max(res, prices[r] - prices[l])

            if(prices[r] < prices[l]){
                l = r
            }
        }

        return res
    }
}
