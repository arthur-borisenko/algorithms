class Sort():

    @staticmethod
    def myFirstSort(arr):
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