class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_list = [0]*26
        ans = -1
        for ch in s:
            index = 97 - ord(ch)
            hash_list[index] += 1

        for i,ch in enumerate(s):
            index = 97 - ord(ch)
            if hash_list[index] == 1:
                ans = i
                break
        return ans
