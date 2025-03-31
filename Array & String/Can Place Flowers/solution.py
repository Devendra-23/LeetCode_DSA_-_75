class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)
        count = 0  # Counter for number of flowers placed

        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)  # First element or left side is empty
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)  # Last element or right side is empty

                if empty_left and empty_right:
                    flowerbed[i] = 1  # Place a flower
                    count += 1  # Increment counter
                    if count >= n:
                        return True

        return count >= n  # Ensure n flowers are placed


# Example usage:
solution = Solution()
print(solution.canPlaceFlowers([0, 0, 0, 0, 0, 1, 0, 0], 0))  # Output: True ✅
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True ✅
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False ✅
