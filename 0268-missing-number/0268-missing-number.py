# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         for i, v in enumerate(nums):
#             if i!=v:
#                 return v-1
#             if v==len(nums)-1:
#                 return v+1



# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         return sum(range(len(nums)+1))- sum(nums)





class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return i
        return len(nums)