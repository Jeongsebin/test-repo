#제4분면 
x=int(input('x좌표를 입력하세요:'))
y=int(input('y좌표를 입력하세요:'))

if x>0:
    if y>0:
        print('제 1사분면')
    elif y<0:
        print('제 4사분면')
    else:
        print('x축 위의 점이다.')
elif x<0:
    if y>0:
        print('제 2사분면')
    elif y<0:
        print('제 3사분면')
    else:
        print('x축 위의 점이다.')
else:
    if y==0:
        print('원점이다.')
    else:
        print('y축 위의 점이다.')
