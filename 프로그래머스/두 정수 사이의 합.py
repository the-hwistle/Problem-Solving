# 프로그래머스 > 코딩테스트 연습 > 연습문제 > 두 정수 사이의 합

def solution(a, b):
    # 가우스 공식에 대입해서 구한다.
    # (첫번째정수+마지막정수)*(정수의개수)/2
    # a와 b의 대소관계는 정해져있지 않으므로 abs()함수를 사용하여 개수를 구한다.
    if a==b:
        answer = a
    else:
        answer = (a+b)*(abs(b-a)+1)//2
    
    return answer
