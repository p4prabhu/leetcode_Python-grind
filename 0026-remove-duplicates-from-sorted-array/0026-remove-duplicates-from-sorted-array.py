
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        # l=len(nums)
        # j=1
        # for i in range(1,l):
        #     if nums[i]!=nums[i-1]:
        #         nums[j]=nums[i]
        #         j+=1
        # return j















class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write=1

        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:
                nums[write]=nums[i]
                write+=1
        return write


    


        

            


        