class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words
        words = s.split()
        print(words)
        # Reverse the order of words
        reversed_words = words[::-1]
        print(reversed_words)
        # Join the reversed words into a string
        reversed_string = ' '.join(reversed_words)
        print(reversed_string)
        return reversed_string
solution = Solution()
result = solution.reverseWords("Hello World")
print(result)