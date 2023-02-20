class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        pre = s[0]
        s_index = 0
        answer  =0
        
        s_count = defaultdict(int)
        
        for i in range(len(s)):
            if s[i] != pre:
                pre = s[i]
                s_index += 1
            s_count[s[i]+str(s_index)] += 1
            
        
        for word  in words:
            valid = True
            w_index = 0
            ltr_count = 0
            for i in range(len(word)):
                ltr_count += 1
                if i+1 == len(word) or word[i+1] != word[i]:
                    key = word[i] + str(w_index)
                    if s_count[key] != ltr_count and (ltr_count > s_count[key] or s_count[key] < 3):
                        valid = False
                        break
                    w_index += 1
                    ltr_count = 0
            if valid and s_index+1 ==  w_index:
                answer += 1
                    
        return answer
        