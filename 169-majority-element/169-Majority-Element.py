class Solution(object):
    def majorityElement(self, nums):

        hash_map = {}

        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else :
                hash_map[i] = 1
            

        return max(hash_map, key=hash_map.get)
        


        
            

            


        



            
        