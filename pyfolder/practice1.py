#작성자 정세빈
hap,i = 0,0

for i in range (1, 101, 2):
    hap += 1

    if hap >= 1000:
        break

print("1~100의 홀수의 합에서 최초로 1000이 넘는 위치:%d" %i)
