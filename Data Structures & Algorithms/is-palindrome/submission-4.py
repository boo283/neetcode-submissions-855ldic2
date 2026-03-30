class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = "".join([char.lower() for char in s if char.isalnum()])
        length = len(valid_s)
        for i, c in enumerate(valid_s[:length//2]):
            if valid_s[i] != valid_s[length-i-1]:
                return False
        return True

        