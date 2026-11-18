import random

from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, counting_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(sort_function, trials=100):
    for _ in range(trials):
        numbers = []

        for i in range(random.randint(0, 50)):
            numbers.append(random.randint(-100, 100))

        old_numbers = numbers.copy()

        result = sort_function(numbers)

        assert result == sorted(old_numbers)
        assert numbers == old_numbers


def check_counting_sort(sort_function, trials=100):
    for _ in range(trials):
        numbers = []

        for i in range(random.randint(0, 50)):
            numbers.append(random.randint(-100, 100))

        old_numbers = numbers.copy()

        result = sort_function(numbers, -100, 100)

        assert result == sorted(old_numbers)
        assert numbers == old_numbers


def check_search(search_function, trials=100):
    for _ in range(trials):
        numbers = []

        for i in range(random.randint(0, 50)):
            numbers.append(random.randint(-100, 100))

        numbers.sort()

        if len(numbers) > 0 and random.randint(0, 1) == 1:
            x = random.choice(numbers)
        else:
            x = 150

        result = search_function(numbers, x)

        if x in numbers:
            assert result >= 0
            assert result < len(numbers)
            assert numbers[result] == x
        else:
            assert result == -1


def check_two_sum(trials=100):
    for _ in range(trials):
        numbers = []

        for i in range(random.randint(0, 50)):
            numbers.append(random.randint(-100, 100))

        if len(numbers) >= 2 and random.randint(0, 1) == 1:
            indexes = random.sample(range(len(numbers)), 2)

            target = numbers[indexes[0]] + numbers[indexes[1]]
        else:
            target = 201

        result1 = two_sum_brute(numbers, target)
        result2 = two_sum_fast(numbers, target)

        assert (result1 is None) == (result2 is None)

        for pair in (result1, result2):
            if pair is not None:
                i, j = pair

                assert i >= 0
                assert i < len(numbers)
                assert j >= 0
                assert j < len(numbers)
                assert i != j
                assert numbers[i] + numbers[j] == target


def main():
    random.seed(42)

    check_sorting(bubble_sort)
    check_sorting(insertion_sort)
    check_sorting(selection_sort)
    check_sorting(merge_sort)

    check_counting_sort(counting_sort)

    check_search(linear_search)
    check_search(binary_search)

    check_two_sum()

    print("OK")


if __name__ == "__main__":
    main()
