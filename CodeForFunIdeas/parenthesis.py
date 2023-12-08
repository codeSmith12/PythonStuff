class Solution:
    def isValid(self, s: str) -> bool:
        if s.count('[') != s.count(']') or s.count('{') != s.count('}') or s.count("(") != s.count(')'):
            return False
        q = []
        for i in range(len(s)):
            if s[i] == '(':
                q.append('(')
            elif s[i] == ')':
                q.pop()
            elif s[i] == '[':
                q.append('[')
            elif s[i] == ']':
                q.pop()
            elif s[i] == '{':
                q.append('{')
            elif s[i] == '}':
                q.pop()

        if len(q) != 0:
            return False
        return True

s = Solution()

print(s.isValid("{[}]}"))
        # list1 = [] # parenth
        # list2 = []  #square
        # list3 = [] # Curly
        # for i in s:
        #     if i == '(':
        #         list1.append(i)
        #     elif i == '[':
        #         list2.append(i)
        #     elif i == '{':
        #         list3.append(i)