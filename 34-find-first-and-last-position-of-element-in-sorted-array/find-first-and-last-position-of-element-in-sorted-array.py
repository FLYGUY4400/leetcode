class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0 
        mid = 0 
        high = len(nums) - 1
        return_list = [] 

        while low <= high: 
            mid = (low + high) // 2

            if nums[mid] == target: 
                bottom_index = mid
                top_index = mid 
                while bottom_index-1 >= 0: 
                    if nums[bottom_index-1] == target: 
                        bottom_index -= 1
                    else: 
                        break 
                while top_index+1 < len(nums):
                    if nums[top_index+1] == target: 
                        top_index +=1 
                    else: 
                        break  
                return_list = [bottom_index, top_index]

                break 
             
            elif nums[mid] < target: 
                low = mid + 1 

            else: 
                high = mid -1 
 
        if len(return_list) == 0: 
            return [-1,-1]
        else: 
            return  return_list
        