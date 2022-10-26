class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dict = {}
        sum = 0
        dict[0] = -1
        
        for i in range(n):
            sum += nums[i]
            
            if (sum % k) in dict:
                if i - dict[(sum % k)] > 1: 
                    # print(nums[dict[(sum % k)] + 1: i + 1])
                    return True
            else:
                dict[(sum % k)] = i
        
        return False