import numpy as np

# 벡터 * 스칼라 가능
array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)
result_array = array * 10
print(result_array)

# 브로드 캐스트
array1 = np.arange(4).reshape(2, 2)
array2 = np.arange(2)
array3 = array1 + array2
print(array3)

# 브로드 캐스트2
array1 = np.arange(0, 8).reshape(2, 4)
array2 = np.arange(0, 8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis=0)
print(array3)
array4 = np.arange(0, 4).reshape(4, 1)
print(array3 + array4)

# 마스킹
array1 = np.arange(16).reshape(4, 4)
print(array1)

array2 = array1 < 10
print(array2)

array1[array2] = 100
print(array1)

# 집계 함수(max, min, sum, mean)
array = np.arange(16).reshape(4, 4)

print(array)
print("열 합계: ", np.sum(array, axis=0))
print("최대값: ", np.max(array))
print("최소값: ", np.min(array))
print("합계: ", np.sum(array))
print("평균값: ", np.mean(array))