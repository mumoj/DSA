def solution(l):
    factorials = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                factorials[i] = factorials[i] + 1
                count = count + factorials[j]

    return count

ar = [1, 2, 3, 4, 5, 6]
print(solution(ar))