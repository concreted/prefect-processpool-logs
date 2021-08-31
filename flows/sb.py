from concurrent.futures import ProcessPoolExecutor, as_completed

def initialize():
    print("Initializing")
    pass

def process(input):
    print(f"Processing: {input}")
    return input

def run_process_pool():
    inputs = [1,2,3,4]
    with ProcessPoolExecutor(
        max_workers=4, initializer=initialize
    ) as pool:
        futures = [pool.submit(process, input) for input in inputs]
        out = [f.result() for f in as_completed(futures)]
    return out
