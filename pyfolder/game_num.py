import random

class Game_num:

    def __init__(self):
        self.human = -1
        self.bot = -1

    def start(self):
        print('0~9 점수 중 컴퓨터가 선택한 무작위 숫자를 맞춰 보세요.')
        self.bot = random.randint(0, 9)

        while (self.bot != self.human):
            print('============================================================')
            self.human = int(input('0부터 9까지의 정수 중 하나 선택하세요.'))

            if self.human < self.bot:
                print('입력하신 숫자가 봇이 고른 숫자보다 작습니다. 다시 시도하세요.')
            elif self.human > self.bot:
                print('입력하신 숫자가 봇이 고른 숫자보다 큽니다. 다시 시도하세요.')
            else:
                print('축하드립니다!! 봇이 고른 숫자를 맞추셨습니다!! :)')
