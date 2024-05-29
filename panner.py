//
n = int(input())
val = []
cost = 0
for i in range(n):
    x = list(map(int,input().split()))
    val.append(x)
x = []
for i in range(n):
    x.append(val[i][1])
x.sort(reverse=1)
for i in range(n):
    cost += x[i] * val[i][0]
print(cost)
//