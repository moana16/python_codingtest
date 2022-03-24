# N과 K가 주어질 때 N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수구하기
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
n,k=map(int,input().split())
result=0

while True:
    # (N==K로 나누어떨어지는 수)가 될때까지 1씩 빼기25
    target=(n//k)*k
    print(target)
    result += (n-target)
    print(result)
    n=target
    print(n)
    if n<k :
        break
    result += 1
    n //= k
    print(n)
result += (n-1)
print(result)