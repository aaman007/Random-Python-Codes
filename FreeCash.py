n = int(input())
cnt=0
a = {}
for i in range(n):
    x = input();
    if(x in a):
        a[x] += 1;
    else:
        a[x] = 1;
    if(a[x]>cnt):
        cnt = a[x]
print(cnt)
