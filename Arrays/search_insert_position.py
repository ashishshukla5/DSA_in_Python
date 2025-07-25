def searchInsert(nums, target):
        start = 0
        end = len(nums) - 1

        while(start <= end):
            mid = (start + end) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
                
        return start