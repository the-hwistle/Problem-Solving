# 프로그래머스 > 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 문제: 오픈채팅방
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42888

# 입력: 채팅방 출입, 닉네임 변경 기록을 담은 문자열 배열
# 출력: 메세지 문자열 배열
def solution(record):
    answer = []
    
    message = {}  # 키: 순서, 값: ['Enter' 또는 'Leave', 유저아이디]
    user = {}     # 키: 유저아이디, 값: 닉네임
    
    for idx, rec in enumerate(record):
        tokens = rec.split(' ')       # Enter/Change일 경우 3개 토큰, Leave일 경우 2개 토큰
        if tokens[0] == 'Leave':
            message[idx] = ['Leave', tokens[1]]
        
        else:
            if tokens[0] == 'Enter':
                message[idx] = ['Enter', tokens[1]]

            user[tokens[1]] = tokens[2]   # 'Enter' 또는 'Change'인 경우 닉네임을 업데이트한다. (조건문으로 분리 가능)

    for idx, m in message.items():
        if m[0] == 'Enter':
            answer.append(user[m[1]]+"님이 들어왔습니다.")
        else:
            answer.append(user[m[1]]+"님이 나갔습니다.")
    
    return answer
