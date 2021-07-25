# 프로그래머스 > 코딩테스트 연습 > 연습문제 > 2016년

# 입력: 월, 일
# 출력: 요일
def solution(a, b):
    # 요일 리스트
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    # 월별 일수 리스트
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 1월1일과 a월b일 사이 날짜 카운트
    count = 0
    # a월 1일이 무슨요일인지 알아내기
    for month, date in enumerate(date):
        # 월 비교
        if month+1 < a:
            count += date
        elif month+1 == a:
            count += b-1
            answer = day[count%7]
            break
    
    return answer
