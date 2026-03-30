class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        sorted_nums = list(sorted(set(nums)))
        longest = 1
        length_tmp = 1
        for i, num in enumerate(sorted_nums[:-1]):
            if sorted_nums[i+1] - num == 1:
                length_tmp += 1
            else:
                if length_tmp > longest:
                    longest = length_tmp
                length_tmp = 1
        if length_tmp > longest:
            longest = length_tmp
        return longest

            
        