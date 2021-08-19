# 프로그래머스 > 코딩테스트 연습 > 탐욕법(Greedy) > 문제: 구명보트
# 문제링크: https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3


# 풀이1) 정확성 통과. 효율성 실패.
from collections import deque

# 입력: 몸무게를 담은 배열, 무게제한
# 출력: 필요한 구명보트 최소 개수
def solution(people, limit):
    answer = 0
    
    n = len(people)
    
    people.sort()
    weights = deque(people)
    
    while len(weights) > 1:
        heaviest = max(weights)
        lightest = min(weights)
        
        if heaviest + lightest > limit:
            weights.pop()    # 마지막 원소 제거
            answer += 1
            
        else:
            weights.pop()    # 마지막 원소 제거
            weights.popleft()   # 첫번째 원소 제거
            answer += 1
        # print(answer)
    
    if len(weights)==1:
        answer += 1
        
    return answer


# 풀이2) 정확성 통과. 효율성 통과 (max, min대신 인덱싱만 조절)

# 입력: 몸무게를 담은 배열, 무게제한
# 출력: 필요한 구명보트 최소 개수
def solution(people, limit):
    answer = 0
    
    people.sort()
    first = 0
    last = len(people)-1
    
    while first < last:
        if people[first] + people[last] > limit:
            last -= 1
            answer += 1
            
        else:
            first += 1
            last -= 1
            answer += 1
    
    if first == last:
        answer += 1
        
    return answer
