import random

number = [1,2,3,4,5,6]
def dice():
    while True:
        computer = random.choice(number)
        print('주사위를 굴리세요. ', computer)
        click = input('다시 굴리시겠습니까? ')
        if click == 'yes':
            continue
        elif click == 'no':
            print('수고하셨습니다.')
            break
dice()
