def longestCommonPrefix(nums):
        nums.sort()
        first = nums[0]
        last = nums[len(nums)-1]
        min_len = min(len(first), len(last))
        i = 0
        while i < min_len and first[i] == last[i]:
            i = i+1
        return first[0:i]