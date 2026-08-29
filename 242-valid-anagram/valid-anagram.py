class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        hash_list = [0] * 26

        for ch1,ch2 in zip(s,t):
            index1 = ord(ch1) - 97
            index2 = ord(ch2) - 97
            hash_list[index1] +=1
            hash_list[index2] -=1

        for count in hash_list:
            if count != 0:
                return False
        
        return True
        
