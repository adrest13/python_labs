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

