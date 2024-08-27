class Solution:
    def isValid(self, s: str) -> bool:
        map_of_statements = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        if len(s) == 0:
            return True
        for i in range(len(s)):
            if s[i] in map_of_statements.values():
                ...