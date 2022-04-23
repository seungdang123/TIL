def solution(N, stages):

    # 내림차순으로 정렬
    stages.sort()

    # 특정 스테이지와 실패율 담는 리스트
    failure_list = []

    for i in range(1, N+1):

        if len(stages) == 0:
            failure_list.append((i,0))
        
        else:
            failure = (stages.count(i) / len(stages))
            failure_list.append((i, failure))
            while i in stages:
                stages.remove(i)
    
    result = []
    failure_list.sort(key = lambda x:x[1], reverse= True)
    print(failure_list)

    for j in failure_list:
        result.append(j[0])

    return result


print(solution(5, [1,2,2,1,3])) 
print(solution(20, [1,2,2,1,3]))

