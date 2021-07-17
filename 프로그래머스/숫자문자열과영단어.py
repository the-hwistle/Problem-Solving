def solution(s):
    eng = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    answer=''    # 리턴값
    word = ''    # 임시버퍼
    char = ''    # 한글자
    for i in range(len(s)):
        char = s[i]
        if char.isdecimal():
            if word:
                answer += eng[word]  # 버퍼에 있는 문자열을 숫자로 변환후 리턴값에 추가
                word = ''            # 버퍼 초기화
            answer+=char    # 숫자는 바로 리턴값에 추가
        else:
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
