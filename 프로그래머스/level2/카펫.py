# 프로그래머스 > 코딩테스트 연습 > 완전탐색 > 카펫
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42842

# 입력: 갈색 격자의 수, 노란색 격자의 수
# 출력: 전체 카펫의 가로, 세로 크기 (가로 >= 세로)
def solution(brown, yellow):
    answer = []
    
    # 노란색 격자의 가로, 세로를 a,b
    # 전체 카펫의 가로, 세로를 c,d라고 하면
    # 전체 카펫의 면적은 (a+2)*(b+2) = brown+yellow이다.
    # 수식을 풀어보면 ab + 2(a+b) + 4 = brown + ab이므로 a와 b는 2(a+b)+4= brown을 만족해야 한다.
    
    # 노란색 격자의 가로, 세로(a와 b)를 구해보자.
    for i in range(1, yellow+1):
        if yellow % i == 0:
            a, b = [yellow//i, i]
            if 2*(a+b)+4 == brown:
                answer = [a+2, b+2]
    
    answer.sort(reverse=True)
    return answer
