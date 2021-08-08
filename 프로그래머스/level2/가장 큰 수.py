# 프로그래머스 > 코딩테스트 연습 > 정렬 > 문제: 가장 큰 수
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    
    # 원소를 str로 변환
    numbers = list(map(str, numbers))
    
    # 원소를 3번 반복한 문자열을 기준으로 내림차순 정렬
    # (예시: 9999 > 5555 > 34343434 > 3333 > 30303030 > 100010001000 )
    numbers.sort(key=lambda x: x*4, reverse=True)
    
    # [0,0,0,0]인 테스트케이스를 통과하기 위함.
    answer = str(int(''.join(numbers)))
        
    return answer
