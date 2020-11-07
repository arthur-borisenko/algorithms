class Sort:

    @staticmethod
    def my_third_sort(arr: []):
        for not_sorted_index in range(0, len(arr)):
            min_index = Sort.find_min_index(arr, not_sorted_index)
            Sort.swap(arr, min_index, not_sorted_index)

    @staticmethod
    def my_second_sort(arr: []):
        output = []
        while len(arr) > 0:
            min_val = min(arr)
            arr.remove(min_val)
            output.append(min_val)
        return output

    @staticmethod
    def my_first_sort(arr: []):
        output = []
        minVal = min(arr)
        maxVal = max(arr) + 1
        for val in range(minVal, maxVal, 1):
            for i in range(Sort.count_in_arr(arr, val)):
                output.append(val)
        return output

    @staticmethod
    def count_in_arr(arr, val):
        cnt = 0
        for el in arr:
            if el == val:
                cnt += 1
        return cnt

    @staticmethod
    def find_min_index(arr: [], not_sorted_index: int):
        elementIndex = None
        for i in range(not_sorted_index, len(arr)):
            if elementIndex is None or arr[elementIndex] > arr[i]:
                elementIndex = i
        return elementIndex

    @staticmethod
    def swap(arr, i1, i2):
        ee = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = ee