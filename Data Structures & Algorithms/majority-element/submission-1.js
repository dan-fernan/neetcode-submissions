class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        let cand = nums[0]
        let count = 1

        for (let i = 1; i < nums.length; i++) {
            if (count == 0) cand = nums[i]
            else if (nums[i] == cand) count++
            else count--
        }
        return cand
    }
}
