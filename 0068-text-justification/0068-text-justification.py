class Solution:
    def justifyASingleLine(self, wordArr, maxWidth, option):
        # option = 0: left justify
        # option = 1: full justify
        extraSpace = maxWidth - (len(wordArr) + sum([len(word) for word in wordArr]) - 1)
        if option == 0:
            return ' '.join(wordArr) + ' ' * extraSpace
        elif option == 1:
            if len(wordArr) == 1:
                return wordArr[0] + ' ' * extraSpace
            else:
                numSpaces = [extraSpace // (len(wordArr) - 1)] * (len(wordArr) - 1)
                for i in range(extraSpace % (len(wordArr) - 1)):
                    numSpaces[i] += 1
                
                result = ''
                for i in range(len(wordArr) - 1):
                    result += wordArr[i] + ' ' * (numSpaces[i] + 1)
                result += wordArr[-1]
                return result
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordArr = []
        result = []
        for word in words:
            if len(wordArr) == 0:
                wordArr.append(word)
            elif len(' '.join(wordArr)) + len(word) + 1 <= maxWidth:
                wordArr.append(word)
            else:
                result.append(self.justifyASingleLine(wordArr, maxWidth, 1))
                wordArr = [word]
        if len(wordArr) > 0:
            result.append(self.justifyASingleLine(wordArr, maxWidth, 0))
        return result