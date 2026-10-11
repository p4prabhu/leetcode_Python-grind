class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        for n in nums:
            i = abs(n)-1
            nums[i]= -1 * abs(nums[i])
        res=[]
        for j, n in enumerate(nums):
                if n > 0:
                    res.append(j+1)
        return res