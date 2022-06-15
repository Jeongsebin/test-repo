dash = '=========================================='
print('반갑습니다. 계좌이체를 위한 정보를 입력하세요')

account = input('1)출금 계좌 번호: ')
bank = input('2)입금 은행: ')
bank_account = input('3)입금 계좌 번호: ')
addressee = input('4)수취인: ')
money = input('5)이체 금액: ')

print('입력하신 정보는 아래와 같습니다.')
print(dash)
print("-출금 계좌 번호: ", account)
print("-입금 은행: ", bank)
print("-입금 계좌 번호: ", bank_account)
print("-수취인: ", addressee)
print("-이체 금: ", money)
print(dash)
