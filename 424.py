class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowStart = 0
        char_freq = {}
        maxlength = 0
        maxrepeatchar = 0

        for windowend in range(len(s)):
            if s[windowend] not in char_freq:
                char_freq[s[windowend]] = 0

            char_freq[s[windowend]] += 1
            maxrepeatchar = max(maxrepeatchar, char_freq[s[windowend]])

            if (windowend - windowStart + 1) - maxrepeatchar > k:
                char_freq[s[windowStart]] -= 1
                windowStart += 1

            maxlength = max(maxlength, windowend - windowStart + 1)

        return maxlength
