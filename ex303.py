n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort() #오름차순 정렬됨
first=data[n-1] #가장큰수
second=data[n-2] #두번째로 큰수

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1) #나눠지지 않음까지 계신

result=0
reslut += (count)*first
result += (m-count)*second

print(result)