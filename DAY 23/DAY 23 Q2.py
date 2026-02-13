import math
import time
import multiprocessing

numbers = [50000, 60000, 55000, 45000, 70000]


def calculate_factorial(n):
    return math.factorial(n)


def run_sequential():
    start_time = time.perf_counter()
    results = []
    for n in numbers:
        results.append(calculate_factorial(n))
    end_time = time.perf_counter()
    return results, end_time - start_time


def run_parallel():
    start_time = time.perf_counter()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(calculate_factorial, numbers)
    end_time = time.perf_counter()
    return results, end_time - start_time


if __name__ == "__main__":
    import sys

    sys.set_int_max_str_digits(0)

    seq_results, seq_duration = run_sequential()

    par_results, par_duration = run_parallel()

    for i, res in enumerate(par_results):
        print(f"Factorial of {numbers[i]} calculated. (Length: {len(str(res))} digits)")

    print("-" * 30)
    print(f"Sequential Time: {seq_duration:.4f} seconds")
    print(f"Parallel Time:   {par_duration:.4f} seconds")