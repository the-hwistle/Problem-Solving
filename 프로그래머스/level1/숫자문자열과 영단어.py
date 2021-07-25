# [프로그래머스]
# 코딩테스트 연습 > 2021 카카오 인턴십 for Tech developers > 문제: 숫자문자열과 영단어(level 1)
# 문제: https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

def solution(s):
    eng = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    answer=''    # 리턴값
    word = ''    # 임시버퍼
    char = ''    # 한글자
    for i in range(len(s)):
        char = s[i]
        if char.isdecimal():
            if word:
                answer += eng[word]  # 버퍼에 있는 문자열을 숫자로 변환후 리턴값에 추가
                word = ''            # 버퍼 초기화
            answer+=char             # 숫자는 바로 리턴값(answer)에 추가
        else:
            if len(word)>=3:         # 딕셔너리eng의 키는 최소 문자가 3개 이상이어야 한다.
                if word in eng.keys():
                    answer += eng[word]
                    word = ''
            word += char
        # print(answer)
        # print('word:', word)
    
    # 마지막 버퍼까지 추가
    if word:
        answer += eng[word]
        
    answer = int(answer)
    
    return answer




# replace함수를 활용한 풀이
def solution2(s):
    eng = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    answer = s
    for key in eng.keys():
        answer = answer.replace(key, eng[key])
        
    return int(answer)
