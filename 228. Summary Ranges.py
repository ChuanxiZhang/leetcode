class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if len(nums) == 1:
            return [str(nums[0])]
        i = 0
        while i < len(nums):
            num = nums[i]
            while i + 1 < len(nums) and nums[i+1] - nums[i] == 1:
                i += 1
            if not nums[i] == num:
                res.append(str(num)+"->"+str(nums[i]))
            else:
                res.append(str(num))
            i += 1
        return res




            
