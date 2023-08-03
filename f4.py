sonlar = list(map(int,input().split()))
a = len(sonlar)
k = sonlar[0:a:2]
print(*k)