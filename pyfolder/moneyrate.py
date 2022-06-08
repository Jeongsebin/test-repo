#환율계산기
money = int(input('환전하고자 하는 금액을 입력하세요 : '))
usd = money / 1141.50
aud = money / 905.15
nzd = money / 836.15

print('미국 :', round(usd,2), 'USD')
print('호주 :', round(aud,2), 'AUD')
print('뉴질랜드 :', round(nzd,2), 'NZD')
