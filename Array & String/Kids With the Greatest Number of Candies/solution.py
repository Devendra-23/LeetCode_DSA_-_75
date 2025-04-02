class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)  # Find the maximum number of candies any kid currently has
        result = []
        
        for candy in candies:
            # Check if giving extraCandies makes the kid have the greatest number of candies
            result.append((candy + extraCandies) >= max_candies)
        
        return result  # Return the final boolean list

# Example usage
solution = Solution()
print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))  # Output: [True, True, True, False, True]
print(solution.kidsWithCandies([4, 2, 1, 1, 2], 1))  # Output: [True, False, False, False, False]
print(solution.kidsWithCandies([12, 1, 12], 10))     # Output: [True, False, True]
