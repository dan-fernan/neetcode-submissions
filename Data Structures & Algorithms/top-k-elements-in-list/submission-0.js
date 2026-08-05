class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map = new Map()
        let res = []

        for (let i = 0; i < nums.length; i++) {
            map.set(nums[i], (map.get(nums[i]) || 0) + 1)
        }
        let sorted = [...map].sort((a, b) => {
            let [, v1] = a
            let [, v2] = b

            return v2 - v1
        })

        for (let i = 0; i < k; i++) {
            res.push(sorted[i][0])
        }
    return res
    }
}
