# 오름차순 정렬하기
scores = [60, 95, 75, 85, 90]
scores.sort()
print(scores)

# 내림차순 정렬하기
scores.sort(reverse=True)
print(scores)

# 원본 복사 후 복사본 리스트 정렬, 복사본 오름차순 정렬
sorted_scores = sorted(scores)
sorted_scores_revers = sorted(scores, reverse=True)
print(scores)
print(sorted_scores)

# 정렬하는 코드로 출력까지 담당하면 안된다 결과: None
print(scores.sort())
print(sorted(scores))

# 리스트 뒤집기
print(scores[::-1])
# [95, 90, 85, 75, 60]

# 리스트 뒤집기 2
scores.reverse()
print(scores)
# [95, 90, 85, 75, 60]

# 복사본 뒤집기
reversed_scores = list(reversed(scores))
print(scores)
# [95, 90, 85, 75, 60]
print(reversed_scores)
# [60, 75, 85, 90, 95]
