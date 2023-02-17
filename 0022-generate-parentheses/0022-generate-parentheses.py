class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def back_track(open_n: int, closed_n: int):
            if open_n == closed_n and open_n == n:
                res.append(''.join(stack))
                return

            if open_n < n:
                stack.append('(')
                back_track(open_n + 1, closed_n)
                stack.pop()

            if closed_n < open_n:
                stack.append(')')
                back_track(open_n, closed_n + 1)
                stack.pop()

        back_track(0, 0)
        return res