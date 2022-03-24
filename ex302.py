# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수 를 찾는 방법
# min() 함수를 이용
n,m=map(int,input().split())

result=0
for i in range(n): #n번씩반복
    data=list(map(int,input().split())) #한줄씩입력받고
    min_value=min(data) #그 줄에서 가장 작은놈을 min_value에 저장
    print(min_value)
    result=max(result,min_value) #그거를 result값이랑 비교해서 가장 큰놈을 result에 넣어줌
print(result) #그러면 당연히 작은 놈들 중에 가장 큰 값을 뱉어냄