# 프로그래머스 > 코딩테스트 연습 > 해시 > 전화번호 목록
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42577

# 입력: 전화번호(str)가 담긴 배열(list)
# 출력: True or False

# 풀이1: 이중 반복문 (정확성 통과, 효율성 실패)
def solution(phone_book):
    # 문자열 길이 순으로 오름차순 정렬
    phone_book.sort(key=lambda x: len(x))
    
    answer = True
    
    # 짧은 문자열 먼저 비교
    for idx, token in enumerate(phone_book):
        l = len(token)
        # 현재 token보다 길이가 긴 문자열의 앞부분을 token과 비교
        for i in range(idx+1, len(phone_book)):
            if token in phone_book[i][0:l]:
                answer = False
    
    return answer
