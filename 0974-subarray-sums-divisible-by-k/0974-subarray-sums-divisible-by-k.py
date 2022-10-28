class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # holds the number of a specific modulo occured so far
        dict = {}
        
        dict[0] = 1
        
        ans = 0
        
        # holds the prefix sum of the array
        sum = 0
        
        for i in range(n):
            # add to the prefix sum
            sum += nums[i]
            
            # check if the modulo is not in the dict, before adding it value to our answer
            if (sum % k) not in dict:
                dict[(sum % k)] = 0
            # add the number of previous modulos to our answer, 
            # because thats how many subarrays we can form
            # starting from this element and going back
            ans += dict[(sum % k)]
            
            # add the current val to our dict
            dict[(sum % k)] += 1
        
        return ans