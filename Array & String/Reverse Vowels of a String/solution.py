class Solution:
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")  # Set of vowels (both lowercase & uppercase)
        s = list(s)  # Convert string to list for in-place modification
        left, right = 0, len(s) - 1  

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]  # Swap vowels
            left += 1
            right -= 1

        return "".join(s)  # Convert list back to string

# Example usage:
solution = Solution()
print(solution.reverseVowels("IceCreAm"))  # Output: "AceCreIm"
print(solution.reverseVowels("leetcode"))  # Output: "leotcede"
