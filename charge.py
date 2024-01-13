n = int(input())
changes = [25, 10, 5, 1]

for _ in range(n):
   money = int(input())
   for i in changes:
      print(money//i, end = ' ')
      money = money % i
    
    