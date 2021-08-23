# 프로그래머스 > 코딩테스트 연습 > 연습문제 > 최댓값과 최솟값
# 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12939

# 입력: 공백으로 구분된 정수들의 문자열
# 출력: 숫자 중 최솟값, 최댓값을 문자열로 반환
def solution(s):
    answer = ''
    
    nums = list(map(int, s.split(' ')))
    
    answer += str(min(nums)) + " "
    answer += str(max(nums))
    
    return answer
