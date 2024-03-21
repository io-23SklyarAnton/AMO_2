import time


def merge_sort(arr: list):
    start = time.time()
    operations = 0

    def sort(array):
        nonlocal operations
        if len(array) < 2:
            operations += 1
            return array
        mid = len(array) // 2
        operations += 1
        return merge(sort(array[:mid]), sort(array[mid:]))

    def merge(arr1, arr2):
        nonlocal operations
        n = len(arr1) + len(arr2)
        result_array = [0] * n
        i1 = 0
        i2 = 0
        operations += 4

        for i in range(n):
            if i1 == len(arr1):
                result_array[i] = arr2[i2]
                i2 += 1
                operations += 4
            elif i2 == len(arr2):
                result_array[i] = arr1[i1]
                i1 += 1
                operations += 4
            else:
                if arr1[i1] < arr2[i2]:
                    result_array[i] = arr1[i1]
                    i1 += 1
                    operations += 5
                else:
                    result_array[i] = arr2[i2]
                    i2 += 1
                    operations += 4
        return result_array

    return sort(arr), time.time() - start, operations
