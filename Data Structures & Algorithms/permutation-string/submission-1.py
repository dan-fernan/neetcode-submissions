class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): 
            return False
        s1_arr_cnt = [0] * 26
        running_arr_cnt = [0] * 26
        


        for i in range(len(s1)):
            s1_arr_cnt[ord(s1[i]) - 97] += 1
            running_arr_cnt[ord(s2[i]) - 97] += 1
        
        key = '#'.join([str(x) for x in s1_arr_cnt])
        if key == '#'.join([str(x) for x in running_arr_cnt]): 
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            running_arr_cnt[ord(s2[left]) - 97] -= 1
            running_arr_cnt[ord(s2[right]) - 97] += 1
            left += 1
            curr_key = '#'.join([str(x) for x in running_arr_cnt])
            print('The current key', curr_key)
            if curr_key == key:
                return True
        return False

            