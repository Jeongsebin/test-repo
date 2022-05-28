s = int(input("초 = "))

h = s//3600

print(h, "시간")

m = (s%3600)//60

print(m, "분")

c = (s%3600)%60

print(c, "초")
