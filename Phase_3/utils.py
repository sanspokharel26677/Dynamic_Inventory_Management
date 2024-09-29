import time
import matplotlib.pyplot as plt

def time_it(task_description):
    """
    A decorator that measures the time taken by a function to execute and displays
    a custom task description along with the time taken.
    
    Args:
    task_description (str): A human-readable description of the task being timed.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()  # Start time before the function runs
            result = func(*args, **kwargs)
            end_time = time.time()  # End time after the function completes
            time_taken = end_time - start_time
            print(f"{task_description}: {time_taken:.6f} seconds")  # Custom message with time
            return result
        return wrapper
    return decorator
    
from memory_profiler import memory_usage

def memory_it(task_description):
    """
    A decorator to measure the memory usage of a function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            mem_usage_before = memory_usage(-1, interval=0.1, timeout=1)
            result = func(*args, **kwargs)
            mem_usage_after = memory_usage(-1, interval=0.1, timeout=1)
            memory_used = mem_usage_after[0] - mem_usage_before[0]
            print(f"{task_description}: Memory used = {memory_used:.6f} MiB")
            return result
        return wrapper
    return decorator

def measure_execution_time(func, input_sizes, *args):
    """
    Measures the time taken by the given function for different input sizes.
    """
    times = []
    for size in input_sizes:
        start_time = time.time()
        func(size, *args)
        end_time = time.time()
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Input size {size}: Time taken = {time_taken:.6f} seconds")
    return times

def plot_execution_times(input_sizes, times, function_name):
    """
    Plots the execution times for different input sizes and saves the graph as an image.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, marker='o', linestyle='-', color='b', label=f'Time taken by {function_name}')
    plt.title(f'Execution Time vs Input Size for {function_name}')
    plt.xlabel('Input Size')
    plt.ylabel('Time Taken (seconds)')
    plt.grid(True)
    plt.legend()
    image_filename = f'{function_name}_execution_time_graph.png'
    plt.savefig(image_filename)
    print(f"Graph saved as {image_filename}")

