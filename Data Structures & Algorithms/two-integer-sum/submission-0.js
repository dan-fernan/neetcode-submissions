class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let map = new Map()
        let arr = []

        for (let i = 0; i < nums.length; i++) {
            map.set(nums[i], i)
        }

        for (let i = 0; i < nums.length; i++) {
            let compl = target - nums[i]

            if (map.has(compl) && map.get(compl) != i) {
                arr.push(Math.min(i, map.get(compl)))
                arr.push(Math.max(i, map.get(compl)))
                return arr
            }
        }
        return arr
    }
}
