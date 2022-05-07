#작성자 정세빈
print('## 안나와 신후의 가위, 바위, 보 게임 ##')
anna = input('안나를 위한 가위,바위,보를 입력하세요: ')
sinhu = input('신후를 위한 가위,바위,보를 입력하세요: ')

if anna == '가위':
    if sinhu == '가위':
        print('무승부')
    elif sinhu == '바위':
        print('신후 승리')
    elif sinhu == '보':
        print('안나 승리')
    else:
        print('신후 값 입력 오류!->',sinhu)
elif anna == '바위':
    if sinhu == '가위':
        print('안나 승리')
    elif sinhu == '바위':
        print('무승부')
    elif sinhu == '보':
        print('신후 승리')
    else:
        print('신후 값 입력 오류!->',sinhu)
elif anna == '보':
    if sinhu == '가위':
        print('신후 승리')
    elif sinhu == '바위':
        print('안나 승리')
    elif sinhu == '보':
        print('무승부')
    else:
        print('신후 값 입력 오류!->',sinhu)
else:
    print('안나 값 입력 오류!->',anna)
