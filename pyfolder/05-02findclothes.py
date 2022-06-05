flag = input('마음에 드는 옷을 찾았나요?(예/아니오): ')

if flag == '예':
    print(':) 축하합니다!!')

    price = input('가격이 얼마인가요?: ')

    if int(price) <= 100000:
        print('구매합니다.')
    else:
        print('포기합니다.')

elif flag == '아니오':
    print(':( 아쉽군요.')
else:
    print("'예'또는 '아니오'만 입력하시오")
