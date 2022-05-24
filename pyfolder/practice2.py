import random

user_a=random.randrange(1, 7)
user_b=random.randrange(1, 7)

print('A의 주사위의 숫자는 %d입니다.' %user_a)
print('B의 주사위의 숫자는 %d입니다.' %user_b)

if user_a > user_b:
    print('A가 이겼습니다.')
elif user < user_b:
    print('B가 이겼습니다.')
else:
    print('둘이 비겼습니다.')
