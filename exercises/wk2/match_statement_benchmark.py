import time
import logging

def benchmark_methods():
    # Test data
    test_values = list(range(1, 1000)) * 100
    
    # Method 1: Dictionary
    def dict_method(value):
        mapping = {i: f"Value {i}" for i in range(1, 1000)}
        return mapping.get(value, "Unknown")
    
    # Method 2: If-elif chain (simplified)
    def if_elif_method(value):
        if value < 250:
            return f"Value {value}"
        elif value < 500:
            return f"Value {value}"
        elif value < 750:
            return f"Value {value}"
        else:
            return f"Value {value}"
    
    # Method 3: Match
    def match_method(value):
        match(value):
            case int() if value < 250:
                return f"Value {value}"
            case int() if value < 500:
                return f"Value {value}"
            case int() if value < 750:
                return f"Value {value}"
        return f"Value {value}"

    # Benchmark dictionary method
    start = time.time()
    for value in test_values:
        result = dict_method(value)
    dict_time = time.time() - start
    
    # Benchmark if-elif method
    start = time.time()
    for value in test_values:
        result = if_elif_method(value)
    if_elif_time = time.time() - start
    
    # Benchmark match method
    start = time.time()
    for value in test_values:
        result = match_method(value)
    match_time = time.time() - start

    print(f"Dictionary method: {dict_time:.4f} seconds")
    print(f"If-elif method: {if_elif_time:.4f} seconds")
    print(f"Match method: {match_time:.4f} seconds")
    print(f"Dictionary is {if_elif_time/dict_time:.2f}x faster")

# Note: Run this to see actual performance differences
def main():
    # logger = logging.getLogger(__name__)
    # logging.basicConfig(filename='match_statement_benchmark.log', level=logging.INFO)
    # logging.info('Started')
    benchmark_methods()
    # logger.info('Finished')

if __name__ == "__main__":
    main()
