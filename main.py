
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
     
    index = [-1,-1]
    for element in range(len(nums)-1):
        for element2 in range(element,len(nums)):
            if target == nums[element] + nums[element2]:
                index[0] = element
                index[1] = element2
    return index

print(twoSum([3,2,4], 6))
