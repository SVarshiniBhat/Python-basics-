def performBubbleSort(nums):
    n = len(nums)
   
    for fixThisIndex in range(n - 1, 0, -1):
        
        for index in range(fixThisIndex):
           
            if nums[index] > nums[index + 1]:
                temp = nums[index]
                nums[index] = nums[index + 1]
                nums[index + 1] = temp
        print(*nums)
 
nums = list(map(int, input().split()))
print("Before sorting:")
print(*nums)
  
performBubbleSort(nums)
 
print("After sorting:")
print(*nums)
