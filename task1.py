
# Сложность алгоритма O(1)
def task(array):
    len_arr = len(array)
    return (len(array) - len(bin(int(array, 2) ^ int('1'*len_arr, 2))[2:]))

print(task("1100"))
print(task("111111111111111111111111100000000"))

