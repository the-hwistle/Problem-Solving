# 문제: https://leetcode.com/problems/valid-parentheses/submissions/
# 문제 설명: 입력된 문자열의 괄호짝이 맞는지 여부 출력

class Solution:
    def isValid(self, s: str) -> bool:
        # 왼쪽 괄호
        left = ['(', '[', '{']
        right = [')', ']', '}']
        
        # 빈 스택
        stack = []
        answer = True
        
        # 왼쪽부터 문자 확인
        for token in list(s):
            # 왼쪽 괄호면 push
            if token in left:
                stack.append(token)
                
            # 오른쪽 괄호면
            elif token in right:
                # 스택이 비어있는지 확인
                if stack == []:
                    answer = False
                    break
                # 우선 스택의 top이 왼쪽괄호인지 확인
                elif stack[-1] in left:
                    # 가장가까운 왼쪽괄호가 오른쪽괄호와 짝이 맞는지 확인
                    if stack[-1] == left[right.index(token)]:
                        stack.pop(-1)
                    else:
                        answer = False
                        break
                else:
                    answer = False
                    break
        
        # 스택에 제거안된 왼쪽괄호가 남은 경우
        if stack!=[] and stack[-1] in left:
            answer = False
        
        return answer
                    
