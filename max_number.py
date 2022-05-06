from itertools import permutations

answer = []

def solution(numbers):
    numbers = list(map(str,numbers))
    arr = []
    arr = ["".join(list(i)) for i in permutations(numbers, len(numbers))]

    numbers = str(max(map(int, arr)))
    return print(numbers)

solution([3, 10, 2])