n = int(input()) ##입력
a= 1 ##비교변수
count_six = 1  ##배수값
i= 1 ##최소개수방

while n > a:
    count_six = 6*i 
    a += count_six
    i += 1
    
    
print(i)
