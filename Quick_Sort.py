# 왼쪽 기준 Quick sort
def quick_sort_left_pivot(arr):
    arr = arr[:]
    comparisons = [0]

    def partition(low, high):
        pivot = arr[low]
        left = low + 1
        right = high

        print("\n[Partition 시작 - Left Pivot] 구간:", arr[low:high+1], ", Pivot:", pivot)

        while True:
            while left <= right and arr[left] < pivot:
                comparisons[0] += 1
                left += 1
            if left <= right:
                comparisons[0] += 1

            while left <= right and arr[right] > pivot:
                comparisons[0] += 1
                right -= 1
            if left <= right:
                comparisons[0] += 1

            if left >= right:
                break

            print("  → Swap:", arr[left], "<->", arr[right])
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        print("  → Pivot swap:", arr[low], "<->", arr[right])
        arr[low], arr[right] = arr[right], arr[low]
        print("[Partition 완료] 결과:", arr[low:high+1])
        return right

    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(arr) - 1)
    return arr, comparisons[0]


def quick_sort_right_pivot(arr):
    arr = arr[:]
    comparisons = [0]

    def partition(low, high):
        arr[low], arr[high] = arr[high], arr[low]
        pivot = arr[low]
        left = low + 1
        right = high

        print("\n[Partition 시작 - Right Pivot] 구간:", arr[low:high+1], ", Pivot:", pivot)

        while True:
            while left <= right and arr[left] < pivot:
                comparisons[0] += 1
                left += 1
            if left <= right:
                comparisons[0] += 1

            while left <= right and arr[right] > pivot:
                comparisons[0] += 1
                right -= 1
            if left <= right:
                comparisons[0] += 1

            if left >= right:
                break

            print("  → Swap:", arr[left], "<->", arr[right])
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        print("  → Pivot swap:", arr[low], "<->", arr[right])
        arr[low], arr[right] = arr[right], arr[low]
        print("[Partition 완료] 결과:", arr[low:high+1])
        return right

    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(arr) - 1)
    return arr, comparisons[0]


def quick_sort_median_pivot(arr):
    arr = arr[:]
    comparisons = [0]

    def median_of_three(low, high):
        mid = (low + high) // 2
        a = arr[low]
        b = arr[mid]
        c = arr[high]
        if (a <= b <= c) or (c <= b <= a):
            return mid
        elif (b <= a <= c) or (c <= a <= b):
            return low
        else:
            return high

    def partition(low, high):
        pivot_index = median_of_three(low, high)
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
        pivot = arr[low]
        left = low + 1
        right = high

        print("\n[Partition 시작 - Median Pivot] 구간:", arr[low:high+1], ", Pivot:", pivot)

        while True:
            while left <= right and arr[left] < pivot:
                comparisons[0] += 1
                left += 1
            if left <= right:
                comparisons[0] += 1

            while left <= right and arr[right] > pivot:
                comparisons[0] += 1
                right -= 1
            if left <= right:
                comparisons[0] += 1

            if left >= right:
                break

            print("  → Swap:", arr[left], "<->", arr[right])
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        print("  → Pivot swap:", arr[low], "<->", arr[right])
        arr[low], arr[right] = arr[right], arr[low]
        print("[Partition 완료] 결과:", arr[low:high+1])
        return right

    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(arr) - 1)
    return arr, comparisons[0]


# main 부분
if __name__ == "__main__":
    sample = [6, 11, 42, 26, 31, 41, 16, 4, 8, 51]

    print("\n --- 왼쪽 기준 Quick Sort ---")
    result, count = quick_sort_left_pivot(sample)
    print("\n정렬 결과:", result, ", 비교 횟수:", count)

    print("\n--- 오른쪽 기준 Pivot Quick Sort ---")
    result, count = quick_sort_right_pivot(sample)
    print("\n정렬 결과:", result, ", 비교 횟수:", count)

    print("\n--- 중간값 기준 Pivot Quick Sort ---")
    result, count = quick_sort_median_pivot(sample)
    print("\n정렬 결과:", result, ", 비교 횟수:", count)
