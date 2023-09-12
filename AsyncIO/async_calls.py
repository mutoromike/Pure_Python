import asyncio
import time


def process_item(item):
    # Blocking operation here
    # ...
    print(f"Sleeping for: {item}")
    time.sleep(item)


async def process_items(items):
    print("Processing items...")
    start = time.perf_counter()
    # Create a task for each item to be processed
    loop = asyncio.get_event_loop()
    tasks = []
    for item in items:
        task = loop.run_in_executor(None, process_item, item)
        task = asyncio.wait_for(task, timeout=2)
        tasks.append(task)

    # Wait for all tasks to complete
    for future in asyncio.as_completed(tasks):
        try:
            await future
        except asyncio.TimeoutError:
            print("A task timed out and was cancelled.")
    end = time.perf_counter()
    print(f"Processed {len(items)} items in {end - start} seconds")


# Example usage
items = [1, 2, 3, 4, 5]
asyncio.run(process_items(items))
