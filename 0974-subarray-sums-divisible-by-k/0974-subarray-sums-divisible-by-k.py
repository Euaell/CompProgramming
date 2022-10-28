class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # holds the number of a specific modulo occured so far
        dict = {}
        
        dict[0] = 1
        
        ans = 0
        
        # holds the prefix sum of the array
        mod = 0
        
        for i in range(n):
            # add to the prefix sum's modulo
            mod = (mod + nums[i]) % k
            
            # check if the modulo is not in the dict, before adding it value to our answer
            if mod not in dict:
                dict[mod] = 0
                
            # add the number of previous modulos to our answer, 
            # because thats how many subarrays we can form
            # starting from this element and going back
            ans += dict[mod]
            
            # add the current val to our dict
            dict[mod] += 1
        
        return ans