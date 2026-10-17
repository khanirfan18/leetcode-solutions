class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive_arr = []
        negative_arr = []
        result = []
        for num in nums:
            if num >= 0:
                positive_arr.append(num)
            else:
                negative_arr.append(num)

        i = 0
        while i < len(positive_arr) :
            result.append(positive_arr[i])
            result.append(negative_arr[i])
            i+=1

        return result


                

         




