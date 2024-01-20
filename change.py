###백준

N, B =map(int, input().split())
x  = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while N: 
    x +=str(arr[N%B])
    N//=B
print(x[::-1])