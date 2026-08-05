class MyHashSet {

    constructor() {
        this.set = []
    }
        
    /**
     * @param {number} key
     * @return {void}
     */
    add(key) {
        if (!this.contains(key)) this.set.push(key)
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        this.set = this.set.filter((elt) => elt != key)
    }

    /**
     * @param {number} key
     * @return {boolean}
     */
    contains(key) {
        for (let i = 0; i < this.set.length; i++) {
            if (this.set[i] == key) return true
        }
        return false
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
