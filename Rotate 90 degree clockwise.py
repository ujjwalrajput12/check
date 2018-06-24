##Rotate 90 degree clockwise
n,m = map(int,input().split())
l = []
for i in range(n):
    k = []
    for j in range(m):
        k.append(int(input()))
    l.append(k)
print(list(zip(*l[::-1])))
  
