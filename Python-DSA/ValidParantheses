from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
 
        for i in s:
            if i in ['}', ']', ')']:
                if not q:
                    return False
                if i == '}':
                    if q.pop() == '{':
                        continue
                    else:
                        return False
                elif i == ']':
                    if q.pop() == '[':
                        continue
                    else:
                        return False
                else:
                    if q.pop() == '(':
                        continue
                    else:
                        return False
            else:
                q.append(i)
        if q:
            return False

        else:
            return True