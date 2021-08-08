# 프로그래머스 > 코딩테스트 연습 > 정렬 > 문제: 가장 큰 수
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    
    # 원소를 str로 변환
    numbers = list(map(str, numbers))
    
    # 원소를 3번 반복한 문자열을 기준으로 내림차순 정렬
    # (예시: 999 > 555 > 343434 > 333 > 303030 )
    numbers.sort(key=lambda x: x*3, reverse=True)

    answer = ''.join(numbers)
    
    return answer
