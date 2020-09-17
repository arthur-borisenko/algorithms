class Sort():

    @staticmethod
    def sort3(arr):
        output = []
        for val in range(min(arr), max(arr) + 1, 1):
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