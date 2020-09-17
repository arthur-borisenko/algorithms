class Sort():

    @staticmethod
    def my_third_sort(arr: []):
        output = [] # do not use additional memory
        while len(arr) > 0:
            min_val = min(arr)
            arr.remove(min_val)
            output.append(min_val)
        return output

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
