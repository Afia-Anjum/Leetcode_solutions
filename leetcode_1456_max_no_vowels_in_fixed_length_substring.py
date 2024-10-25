class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(char):
            vowel = ['a', 'e', 'i', 'o', 'u']
            if char in vowel:
                return True
            else:
                return False

        vowel_cnt = 0
        s = list(s)
        left = right = length = answer = 0
        for right in range(len(s)):
            if is_vowel(s[right]):
                vowel_cnt += 1
            length = right - left + 1
            if length >= k:
                answer = max(answer, vowel_cnt)
                if is_vowel(s[left]):
                    vowel_cnt -= 1
                left += 1
        return answer