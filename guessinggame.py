import random

user = int(input('숫자를 입력하세요: '))
number = [1,2,3,4,5,6,7,8,9,10]
score = 100
while True:
    computer = random.choice(number)
    if computer != user:
        score -= 10
        print('점수 : ', score)
        int(input('다시 추측하세요: '))
    else:
        print('사용자와 컴퓨터의 숫자가 같습니다.')
        print('점수 : ', score)
        break
        
