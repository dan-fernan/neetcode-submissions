class Solution {
    /**
     * @param {character[]} s
     * @return {void} Do not return anything, modify s in-place instead.
     */
    reverseString(s) {
        let lPtr = 0
        let rPtr = s.length - 1

        while (lPtr < rPtr) {
            let temp = s[lPtr]
            s[lPtr] = s[rPtr]
            s[rPtr] = temp

            lPtr++
            rPtr--
        }
    }
}
