import time


def merge_sort(arr: list):
    start = time.time()

    def sort(array):
        if len(array) < 2:
            return array
        mid = len(array) // 2
        return merge(sort(array[:mid]), sort(array[mid:]))

    def merge(arr1, arr2):
        n = len(arr1) + len(arr2)
        result_array = [0] * n
        i1 = 0
        i2 = 0

        for i in range(n):
            if i1 == len(arr1):
                result_array[i] = arr2[i2]
                i2 += 1
            elif i2 == len(arr2):
                result_array[i] = arr1[i1]
                i1 += 1
            else:
                if arr1[i1] < arr2[i2]:
                    result_array[i] = arr1[i1]
                    i1 += 1
                else:
                    result_array[i] = arr2[i2]
                    i2 += 1
        return result_array

    return sort(arr), time.time() - start