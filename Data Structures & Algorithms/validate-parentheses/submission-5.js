class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const hashmap = {")": "(", "]":"[", "}":"{"}
        let stack = []

        for (const c of s){
            if (!(c in hashmap)){
                stack.push(c)
            }else{
                if(!stack.length || hashmap[c] != stack[stack.length - 1]){
                    return false
                }else{
                    stack.pop()
                }
            }
        }

        return !stack.length
    }
}
