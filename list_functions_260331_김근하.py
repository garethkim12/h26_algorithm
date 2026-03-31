#1번 문항
def getindex(num_list, target): # 함수 정의
    if target in num_list:      # 리스트 상에 값이 없을 때 구현
        return num_list.index(target) #있으면 target 위치값을 반환
    else:
        return -1 #없으면 -1 반환


#2번 문항
def getMax(num_list):
    max_a = num_list[0]  
    for i in range(1, len(num_list)):
        if max_a < num_list[i]:
            max_a = num_list[i]
    return max_a
        

#3번 문항
def getMin(num_list):
    min_a = num_list[0]  
    for i in range(1, len(num_list)):
        if min_a > num_list[i]:
            min_a = num_list[i]
    return min_a
        

#4번 문항
def countGT(num_list, target):
    # 1. 개수를 저장할 변수를 0으로 초기화
    count = 0
    
    # 2. 리스트의 모든 요소를 하나씩 꺼내서 반복 (순차 탐색)
    for i in num_list:
        # 3. 만약 현재 요소(i)가 기준값(target)보다 크다면
        if target < i:
            # 4. 카운트를 1 증가
            count += 1
            
    # 5. 최종적으로 세어진 개수를 반환
    return count


#5번 문항
def sumList(num_list):
   sum = 0
   for i in num_list:
    sum += i
   return sum


#6번 문항
def swapList(num_list):
    return num_list[::-1]


num_list = [1,2,3,4,5,6]
print(swapList(num_list))