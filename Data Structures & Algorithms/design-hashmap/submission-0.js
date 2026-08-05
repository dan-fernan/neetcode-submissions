class MyHashMap {
    constructor() {
        this.map = []
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        if (this.get(key) == -1) this.map.push([key, value])
        else {
            for (let i = 0; i < this.map.length; i++) {
                if (this.map[i][0] == key) this.map[i][1] = value
            }
        }
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        for (let i = 0; i < this.map.length; i++) {
            if (this.map[i][0] == key) return this.map[i][1]
        }
        return -1
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        this.map = this.map.filter((elt) => elt[0] != key)
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
