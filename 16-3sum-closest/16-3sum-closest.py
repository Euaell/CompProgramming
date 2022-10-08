class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        print(n)
        nums.sort()
        ans = -1
        dif = inf
        
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else: return sum
                
                tmp = abs(sum - target)
                if (dif > tmp): 
                    ans = sum
                    dif = tmp
            
#         for i in range(n - 2):
            
#             left = i + 1
#             right = n - 1
#             while (left < right):
#                 sum = nums[i] + nums[left] + nums[right]
#                 if (sum > target):
#                     right -= 1
#                 elif (sum < target):
#                     left += 1
#                 else: return sum
                
#                 if (abs(ans - target) > abs(sum - target)): 
#                     ans = sum
            
        return ans