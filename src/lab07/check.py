import random

from src.lab07.sorting import bubble_sorted, insertion_sorted, selection_sorted, merge_sorted, counting_sorted
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(fn, trials=100) -> None:
    for _ in range(trials):
        nums = [random.randint(-100, 100) for z in range(random.randint(0, 50))]
        old = nums.copy()

        assert fn(nums) == sorted(nums)
        assert nums == old


def check_counting_sorted(fn, trials=100) -> None:
    for _ in range(trials):
        nums = [random.randint(-100, 100) for z in range(random.randint(0, 50))]
        old = nums.copy()

        assert fn(nums, -100, 100) == sorted(nums)
        assert nums == old


def check_search(fn, trials=100) -> None:
    for i in range(trials):
        nums = sorted(random.randint(-100, 100) for z in range(random.randint(0, 50)))
        x = random.choice(nums) if nums and random.randint(0, 1) else 150

        result = fn(nums, x)

        if x in nums:
            assert 0 <= result < len(nums)
            assert nums[result] == x
        else:
            assert result == -1


def check_two_sum(trials=100) -> None:
    for i in range(trials):
        nums = [random.randint(-100, 100) for z in range(random.randint(0, 50))]

        if len(nums) >= 2 and random.randint(0, 1):
            i, j = random.sample(range(len(nums)), 2)
            target = nums[i] + nums[j]
        else:
            target = 201

        a = two_sum_brute(nums, target)
        b = two_sum_fast(nums, target)

        assert (a is None) == (b is None)

        for result in (a, b):
            if result is not None:
                i, j = result
                assert 0 <= i < len(nums)
                assert 0 <= j < len(nums)
                assert i != j
                assert nums[i] + nums[j] == target


def main():
    random.seed(42)

    for fn in (bubble_sorted, insertion_sorted, selection_sorted, merge_sorted):
        check_sorting(fn)

    check_counting_sorted(counting_sorted)

    for fn in (linear_search, binary_search):
        check_search(fn)

    check_two_sum()

    print("Accepted")


if __name__ == "__main__":
    main()
