# core/executor.py

from concurrent.futures import ThreadPoolExecutor, as_completed
from core.config import MAX_WORKERS

def run_concurrent(func, items):
    results = {}
    if not items:
        return results

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(func, i): i for i in items}
        for future in as_completed(futures):
            item = futures[future]
            try:
                results[item] = future.result()
            except Exception as e:
                print(f"[!] Error in {func.__name__} for {item}: {e}")
                results[item] = None

    return results
