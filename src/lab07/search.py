def linear_search(nums: list[int], x: int) -> int:
    '''
    Linear search

    Input: nums: list[int], x: int
    Output: int

    Complexity: O(n)
    '''

    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

def binary_search(sorted_nums: list[int], x: int) -> int:
    '''
    Binary search

    Input: sorted_nums: list[int], x: int
    Output: int

    Complexity: O(log n)
    '''

    l = 0
    r = len(sorted_nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1

def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:
    '''
    Searching for two indices that help obtain the required amount (long)

    Input: nums: list[int], target: int
    Output: tuple[int, int] | None

    Complexity: O(n**2)
    '''
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    '''
    Searching for two indices that help obtain the required amount (fast)

    Input: nums: list[int], target: int
    Output: tuple[int, int] | None

    Complexity: O(n)
    '''
    s = {}
    for i in range(len(nums)):
        x = nums[i]
        y = target - x
        if y in s:
            return (s[y], i)
        s[x] = i
    return None