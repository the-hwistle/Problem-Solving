# 프로그래머스 > 코딩테스트 연습 > 연습문제 > 서울에서 김서방 찾기

def solution(seoul):
    # 파이썬에는 리스트 내에서 찾고하자하는 원소의 인덱스를
    # 리스트.index('원소')로 알 수 있다.
    pos = seoul.index('Kim')
    
    answer='김서방은 '+str(pos)+'에 있다'
    return answer
