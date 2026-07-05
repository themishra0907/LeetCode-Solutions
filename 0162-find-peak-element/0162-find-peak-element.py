class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = max(nums)
        index = nums.index(largest)
        return index
