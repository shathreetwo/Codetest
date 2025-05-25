def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시  
    if i == 100:
        return
    print("{0}번째 재귀 함수에서 {1}번째 재귀를 호출합니다.".format(i, i + 1))
    recursive_function(i + 1)
    print("{0}번째 재귀 함수를 종료합니다.".format(i))

recursive_function(1)
