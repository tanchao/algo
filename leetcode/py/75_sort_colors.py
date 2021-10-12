class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        
        red, blue = 0, 2
        cursor, red_index, blue_index = 0, 0, len(nums) - 1
            
        while cursor <= blue_index:
            while nums[red_index] == red:
                red_index += 1
                if red_index >= blue_index: return
            while nums[blue_index] == blue:
                blue_index -= 1
                if red_index >= blue_index: return
            
            if cursor < red_index: cursor = red_index
                
            if nums[cursor] == red:
                nums[cursor] = nums[red_index] 
                nums[red_index] = red
                red_index += 1
            elif nums[cursor] == blue:
                nums[cursor] = nums[blue_index]
                nums[blue_index] = blue
                blue_index -= 1
            else:
                cursor += 1