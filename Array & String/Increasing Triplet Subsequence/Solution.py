class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # smallest so far
            elif num <= second:
                second = num  # second smallest
            else:
                # Found a number greater than both
                return True
        
        return False