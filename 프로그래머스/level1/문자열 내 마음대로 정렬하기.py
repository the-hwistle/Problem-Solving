# 프로그래머스 > 코딩테스트 연습 > 연습문제 > 문자열 내 마음대로 정렬하기
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12915

# 알아둘점
# a.sort()는 a가 정렬되며 아무것도 반환하지 않는다.
# b = sorted(a)는 a는 그대로이고 정렬된 시퀀스가 반환되어 b에 저장된다.

def solution(strings, n):
    # 사전순으로 오름차순 정렬한 strings를
    # 다시 n번째 문자를 기준으로 정렬한다.
    return sorted(sorted(strings), key=lambda x: x[n])
