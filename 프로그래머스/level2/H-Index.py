# 프로그래머스 > 코딩테스트 연습 > 정렬 > 문제: H-Index
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42747

# 입력: 논문의 인용 횟수
# 출력: H-Index (최댓값: 발표한 논문의 수 n)
def solution(citations):
    # 발표한 논문의 수
    n = len(citations)
    
    # h회 이상 인용된 논문
    citations.sort()             # 오름차순 정렬 => i번째 원소는 최소 i이상이다.
    for idx, cited_n in enumerate(citations):   # 첫번째 원소부터 순회
        if cited_n >= n-idx:     # i번째 원소가 n-idx이상이라면 (n=4인경우 n-idx는 4,3,2,1이다.)
            return n-idx         # H-Index는 n-idx이다. (n=4인경우 입력이[4,5,6,7]이라면 H-Index는 4-0=4이다.)

    return 0
