def solution(arr1, arr2):

    answer = []

    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    
    return print(answer)


solution([[1,2],[2,3]], [[3,4],[5,6]])
solution([[0],[1]], [[2],[3]])
solution([[0],[1],[10]], [[2],[3],[100]])
solution([[1,2,3],[2,3,4]], [[3,4,5],[5,6,7]])