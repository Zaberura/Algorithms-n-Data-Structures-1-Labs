
def find_max_sorted_subarray(arr):
    max = 1
    length = 1

    for i in range(1, len(arr)):

        if arr[i] > arr[i - 1]:
            length = length + 1
        else:

            if max < length:
                max = length

            length = 1

    if max < length:
        max = length

    return max



