import heapq
n = int(input())
m = int(input())
v = []
d = []
for _ in range(n):
    v.append(int(input()))
for _ in range(n):
    d.append(int(input()))
heap = []
for i in range(n):
    heapq.heappush(heap,(-v[i],i,1))
total = 0
curr = 0
while curr<m:
    val,i,t = heapq.heappop(heap)
    cval = -val
    if cval<=0:
        break
    total += cval
    nxt_taste = cval - d[i]*t
    heapq.heappush(heap,(-nxt_taste,i,t+1))
    curr += 1
print(total)