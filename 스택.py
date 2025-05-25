stack = []

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력


'''파이썬 리스트에서 [:]는 슬라이싱(slice) 이라고 부르며,
형식은 아래와 같습니다:

list[start:stop:step]
start: 시작 인덱스 (기본값은 0)

stop: 끝 인덱스 (기본값은 리스트 끝)

step: 증감값 (기본값은 1)

🔸 [::-1] 분석
start, stop 없이 step만 -1로 지정

→ 처음부터 끝까지 역순으로 한 칸씩 이동

결과: 리스트를 거꾸로 뒤집음'''
