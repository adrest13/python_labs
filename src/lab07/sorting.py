def bubble_sort(nums: list[int]) -> list[int]:
    '''
    Optimized bubble sort

    Input: list[int]
    Output: list[int]

    Complexity: O(n**2)
    '''
    a = list(nums)
    n = len(a)

    for i in range(n):
        lamp = 0
        for j in range(0, n - (i + 1)):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                lamp = 1

        if (not lamp):
            break

    return a

def selection_sort(nums: list[int]) -> list[int]:
    ''' 
    Selection sort

    Input: nums: list[int]
    Output: list[int]

    Complexity: O(n**2)
    '''
    a = list(nums)
    n = len(a)

    for i in range(n):
        mn = i
        for j in range(i + 1, n):
            if a[j] < a[mn]:
                mn = j

        a[i], a[mn] = a[mn], a[i]

    return a

def insertion_sort(nums: list[int]) -> list[int]:
    '''
    Insertion_sort

    Input: nums: list[int]
    Output: list[int]

    Complexity: O(n**2)
    '''
    a = list(nums)
    n = len(a)

    for i in range(1, n):
        x = a[i]          
        j = i - 1

        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = x

    return a


def merge_sort(nums: list[int]) -> list[int]:
    '''
    Merge sort

    Input: nums: list[int]
    Output: list[int]

    Complexity: O(n log n)
    '''
    a = nums.copy()
    n = len(a)
    step = 1

    while step < n:
        l = 0

        while l < n:
            mid = min(l + step, n)
            r = min(mid + step, n)

            m = []
            i = l
            j = mid

            while i < mid or j < r:
                if j >= r or (i < mid and a[i] <= a[j]):
                    m.append(a[i])
                    i += 1
                else:
                    m.append(a[j])
                    j += 1

            a[l:r] = m
            l += 2 * step

        step *= 2

    return a



def counting_sort(nums: list[int], l: int, r: int) -> list[int]:
    '''
    Counting sort

    Complexity: O(n + k), k = (r - l)
    '''
    count = [0] * (r - l + 1)

    for i in range(len(nums)):
        index = nums[i] - l
        count[index] += 1

    res = []

    value = l
    while value <= r:
        amount = count[value - l]

        for i in range(amount):
            res.append(value)

        value += 1

    return res
