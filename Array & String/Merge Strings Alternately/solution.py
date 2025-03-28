class Solution:
    def mergeAlternately(self, word1, word2):
        merged = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        merged.extend(word1[i:])  # Append remaining characters of word1 (if any)
        merged.extend(word2[j:])  # Append remaining characters of word2 (if any)
        return "".join(merged)

# Example usage:
solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))   # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))   # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))   # Output: "apbqcd"
