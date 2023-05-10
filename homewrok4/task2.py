n = int(input())
a = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    curr_sum = a[i] + a[(i-1)%n] + a[(i+1)%n]
    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)