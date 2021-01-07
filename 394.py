class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ''
        for i in range(len(s) - 1, -1, -1):
            character = s[i]
            if character.isalpha():
                if not stack:  # stack is empty
                    stack.append(character)
                elif stack[-1] not in ['[', ']']:
                    stack[-1] = character + stack[-1]
                else:
                    stack.append(character)
            elif character in [']', '[']:
                stack.append(character)
            else:  # character is digit
                if i == 0:
                    num = character + num
                    stack.pop()
                    stack[-1] = stack[-1] * int(num)
                    stack.pop(-2)
                else:
                    if not s[i - 1].isdigit():
                        num = character + num
                        stack.pop()
                        stack[-1] = stack[-1] * int(num)
                        stack.pop(-2)
                        num = ''
                        if len(stack) > 1:
                            if stack[-2] not in [']', '[']:
                                stack[-2] = stack[-1] + stack[-2]
                                stack.pop()
                    else:
                        num = character + num

            print(num)
            print(stack)
        return ''.join(stack[::-1])
