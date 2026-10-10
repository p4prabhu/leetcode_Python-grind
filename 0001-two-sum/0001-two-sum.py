class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      
        prevmap = {}
        
        for i,j in enumerate(nums):
            diff = target - j
            if diff in  prevmap:
                return [prevmap[diff],i]
            prevmap[j]=i




        