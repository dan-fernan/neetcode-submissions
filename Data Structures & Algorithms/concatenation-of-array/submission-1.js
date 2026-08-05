class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        let concat = new Array(nums.length * 2).fill(0)

        for (let i = 0; i < nums.length; i++) {
            concat[i] = nums[i]
            concat[i + nums.length] = nums[i]
        }
        return concat
    }
}
