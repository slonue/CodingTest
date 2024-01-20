A, B, V = map(int, input().split())

day = (V-B) / (A-B) ##정수형이면 그대로 출력, 아니면 +1

if day == int(day):
    print (int(day))
else:
    print(int(day) +1)