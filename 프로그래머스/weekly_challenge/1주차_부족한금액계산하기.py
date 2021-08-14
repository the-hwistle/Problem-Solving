# 프로그래머스 > 위클리 챌린지 > 1주차. 부족한금액 계산하기
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/82612

# 입력: 처음 이용료, 가지고있는돈, 놀이기구탑승횟수
# 출력: 모자란 금액
def solution(price, money, count):
    
    # price가 x라면, count만큼 탑승하면 (x+2*x+3*x+...+count*x)만큼의 돈이 소모된다.
    # (1+2+3+...+count)는 가우스공식에 의해서 (1+count)*count/2임을 이용하자.
    
    answer = price*(1+count)*count/2 - money
    
    if answer < 0:
        answer = 0
        
    # 위의 조건문 대신
    # answer = max(0, price*(1+count)*count/2 - money)로 대체할 수 있다.
    
    return answer
  
