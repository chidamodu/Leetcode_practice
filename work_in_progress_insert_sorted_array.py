#work in progress!

# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
    
        else:
            q=int(len(nums)/2) #when len(nums) is an even number
            #print(q)
#             else:
#                 q=int(len(nums)/2)+1   #when len(nums) is a odd number
#                 print(q)
            
            
            if nums[q] > target:
                for e in range(0, len(nums[:q])):
                    print(nums[:q])
                    
                    while nums[e] < target:
                        res=nums.index(nums[e])+1
                        
                    elif target < nums[e] and nums.index(nums[e])==0:
                        res=0      
                    else:
                        res=nums.index(nums[e])-1
                    return res
                                      
            else:
                for j in range(0, len(nums[q:])):
                    print(nums[q:])
                    #print(target)
                    if target < nums[j]:
                        #print(nums[j])
                        res=nums.index(nums[e])
                    
                    res=(nums.index(nums[-1]))
                    
                    return res