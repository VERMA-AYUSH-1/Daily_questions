from collections import deque
s="AYUSH"
n=len(s)
q=deque()
q.append("")
for i in range(n):
    m=len(q)
    for j in range(m):
        q.append(q[j]+s[i])
print(q)
print(len(q))


from collections import deque
arr="AYUSH"
n = len(arr)
q = deque()
q.append([]) 

for i in range(n):
    m = len(q)
    for j in range(m):
        ns = q[j] + [arr[i]]
        q.append(ns)

print(q)
print(len(q))
