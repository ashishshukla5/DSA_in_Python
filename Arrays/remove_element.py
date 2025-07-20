def removeElement(nums, val):
        index = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[index] = nums[i]
                index = index+1
        return index