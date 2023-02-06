class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set: Set[str] = set(words)
        # Add the empty string, which is a valid word in our solution.
        words_set.add("")

        @lru_cache(None)
        def dp(word: str) -> int:
            if len(word) <= 1:
                return 1

            lengths: List[int] = []
            for i in range(len(word)):
                new_word: str = word[:i] + word[i+1:]
                if new_word in words_set:
                    lengths.append(1 + dp(new_word))
            if lengths:
                return max(lengths)
            return 1

        # Compute the chain length for each word and return the maximum.
        res: int = 1
        for word in words:
            res = max(res, dp(word))
        return res