class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map = new Map()

        for (let num of nums) {
            map.set(num, (map.get(num) || 0) + 1)
        }
        return [...map].sort((a, b) => b[1] - a[1]).map(([k, v]) => k).slice(0,k)
    }
}
