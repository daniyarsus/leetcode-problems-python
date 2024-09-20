class Solution:
    def isValid(self, s: str) -> bool:
        def validate(data: str, n: int = 0) -> bool:
            if n >= len(data):
                return

            if data[n] in ["{", "}", "(", ")", "[", "]"]:
                if data[n] == "(" and data[n+1] == ")":
                    pass
                elif data[n] == "[" and data[n+1] == "]":
                    pass
                elif data[n] == "{" and data[n+1] == "}":
                    pass
                else:
                    return False
            else:
                return False

            return validate(data, n + 1)

        return validate(s)


sol = Solution()
print(sol.isValid("()[]"))
