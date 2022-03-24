# 완전 탐색 알고리즘 : 가능한 경우의 수를 모두 검사해보는 탐색 방법
# N 입력받기
h=int(input())
# 시, 분, 초 중 단순히 시각을 1씩 증가시키면서 h시간에 3이 하나라도 포함되어 있는지 확인
# 3중 반복문을 이용해 계산

count=0
for i in range(h+1):
    for j in range(60) :
        for k in range(60):
            #매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)

