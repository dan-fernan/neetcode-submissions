class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
        let otherPos = 0

        for (let i = 0; i < nums.length; i++) {
            if (nums[i] != val) nums[otherPos++] = nums[i]
        }

        return otherPos
    }
}
