class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let check = new Array(26).fill(0)

        if (s.length != t.length) return false

        for (let i = 0; i < s.length; i++) {
            check[s.charCodeAt(i) - 97]++
            check[t.charCodeAt(i) - 97]--
        }
        return check.every(elt => elt == 0)
    }
}
