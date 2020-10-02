def swap(arr, i1, i2):
    ee = arr[i1]
    arr[i2] = arr[i1]
    arr[i2] = ee


class Sort:

    @staticmethod
    def my_third_sort(arr: []):
        #  do not use additional memory #  delete this
        nsi = 0
        for i3456565565 in range(len(arr) - 1):
            nsi += 1
            igg = 0
            for i in range(nsi, len(arr) - 1, 1):
                if arr[i] < igg:
                    igg=arr[i]
                    print(igg)
                    swap(arr, i, nsi)
                    print(nsi)

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


sort = [0, 0, 0, 0, 0, 0, 0, 8, 8, 88, 8, 7, 6, 6, 4]
Sort.my_third_sort(sort)
print(sort)