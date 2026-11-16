import random
import timeit
import os

from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import (
    bubble_sort, insertion_sort, selection_sort,
    counting_sort, merge_sort
)
from src.lab07.search import (
    linear_search, binary_search,
    two_sum_brute, two_sum_fast
)


def measure(func, runs=1, repeats=5):
    return min(timeit.repeat(func, number=runs, repeat=repeats)) / runs


def bench_sorts(n):
    numbers = [random.randint(-10000, 10000) for _ in range(n)]
    results = []

    algorithms = {
        "sorted": sorted,
        "merge_sort": merge_sort,
        "bubble_sort": bubble_sort,
        "insertion_sort": insertion_sort,
        "selection_sort": selection_sort
    }

    for name, func in algorithms.items():
        if n >= 100000 and name in (
            "bubble_sort", "insertion_sort", "selection_sort"
        ):
            seconds = "> 60.0"
        else:
            runs = 100 if name == "sorted" else 1
            repeats = 1 if n >= 100000 else 5

            seconds = measure(
                lambda: func(numbers.copy()), runs, repeats
            )

        results.append(("sort", n, name, seconds))

    return results


def bench_counting():
    n = 1000000
    numbers = [random.randint(0, 100) for _ in range(n)]

    return [
        ("count", n, "sorted",
         measure(lambda: sorted(numbers.copy()), 5, 3)),

        ("count", n, "counting_sort",
         measure(lambda: counting_sort(numbers.copy(), 0, 100), 5, 3))
    ]


def bench_search(n):
    numbers = [random.randint(-100000, 100000) for _ in range(n)]
    queries = [random.randint(-100000, 100000) for _ in range(10000)]

    def run_search(func, data):
        for value in queries:
            func(data, value)

    linear_time = measure(
        lambda: run_search(linear_search, numbers), 1, 1
    )

    sort_time = measure(lambda: sorted(numbers), 1, 1)
    ordered = sorted(numbers)

    binary_time = measure(
        lambda: run_search(binary_search, ordered), 10, 1
    )

    return [
        ("search", n, "linear", linear_time),
        ("search", n, "sort_only", sort_time),
        ("search", n, "binary", binary_time)
    ]


def bench_two_sum(n):
    numbers = random.sample(range(-100000, 100000), n)

    i, j = random.sample(range(n), 2)
    target = numbers[i] + numbers[j]

    brute_time = measure(
        lambda: two_sum_brute(numbers.copy(), target), 1, 1
    )

    fast_time = measure(
        lambda: two_sum_fast(numbers.copy(), target), 100, 1
    )

    return [
        ("sum", n, "two_sum_brute", brute_time),
        ("sum", n, "two_sum_fast", fast_time)
    ]


def main():
    random.seed(42)
    results = []

    print("Проверка сортировок...")
    for n in (1000, 10000, 100000):
        results.extend(bench_sorts(n))

    print("Проверка Counting Sort...")
    results.extend(bench_counting())

    print("Проверка поиска...")
    results.extend(bench_search(100000))

    print("Проверка Two Sum...")
    for n in (1000, 10000):
        results.extend(bench_two_sum(n))

    print(f"\n{'task':<10} | {'n':<10} | {'impl':<15} | seconds")
    print("-" * 55)

    for task, n, name, seconds in results:
        if isinstance(seconds, str):
            value = seconds
        else:
            value = f"{seconds:.6f}"

        print(f"{task:<10} | {n:<10} | {name:<15} | {value}")

    os.makedirs("data/lab07", exist_ok=True)

    write_csv(
        results,
        "data/lab07/bench.csv",
        header=("task", "n", "impl", "seconds")
    )

    print("\nРезультаты сохранены в data/lab07/bench.csv")


if __name__ == "__main__":
    main()