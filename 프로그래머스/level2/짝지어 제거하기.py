# 프로그래머스 > 코딩테스트 연습 > 2017 팁스타운 > 문제: 짝지어 제거하기
# 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    if len(s) % 2 == 1:
        return 0
    
    stack = list(s)
    temp = []
    while stack != []:
        if temp == []:
            temp.append(stack.pop())
        
        if temp[-1] == stack[-1]:
            temp.pop()
            stack.pop()
        
        else:
            temp.append(stack.pop())
            
    if temp == []:
        return 1
    else:
        return 0
