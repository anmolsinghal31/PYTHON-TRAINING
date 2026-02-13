import requests
import time
from concurrent.futures import ThreadPoolExecutor

urls = [
    "https://example.com/data1",
    "https://example.com/data2",
    "https://example.com/data3",
    "https://example.com/data4"
]


def download_file(url):
    """Downloads content from a URL and saves it to a file."""
    try:
        response = requests.get(url, timeout=10)
        # Extract filename from URL (e.g., 'data1')
        filename = f"{url.split('/')[-1]}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        return f"Successfully downloaded {url}"
    except Exception as e:
        return f"Failed to download {url}: {e}"


def run_sequential():
    print("Starting sequential downloads...")
    start_time = time.perf_counter()
    for url in urls:
        download_file(url)
    end_time = time.perf_counter()
    return end_time - start_time


def run_threaded():
    print("Starting threaded downloads...")
    start_time = time.perf_counter()
    # Using ThreadPoolExecutor to manage threads concurrently
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        executor.map(download_file, urls)
    end_time = time.perf_counter()
    return end_time - start_time


if __name__ == "__main__":
    # 1. Execute Sequential
    seq_time = run_sequential()

    # 2. Execute Threaded
    thread_time = run_threaded()

    # 3. Print Results
    print("-" * 30)
    print(f"Sequential Time: {seq_time:.4f} seconds")
    print(f"Threaded Time:   {thread_time:.4f} seconds")
    print(f"Improvement:     {((seq_time - thread_time) / seq_time) * 100:.1f}%")