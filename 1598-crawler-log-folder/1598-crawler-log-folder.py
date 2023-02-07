class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        count = 0
        for vs in logs:
            if vs == "../":
                count = 0 if count == 0 else count - 1
            elif vs == "./":
                continue
            else:
                count += 1
        
        return count