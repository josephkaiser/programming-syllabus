from log_config import setup_logger

logger = setup_logger(__name__)

# Helper functions FIRST
def do_something():
    logger.debug("Doing something...")
    #tell log when function occuring.
    return 42

def process_data(data):
    logger.info(f"Processing: {data}")
    #Example of restating argument to function in definition and printing to log
    return data * 2

def main():
    logger.info("Application started") # Initial print
    
    try:
        result = do_something()
        logger.info(f"Success: {result}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise
    
    logger.info("Application finished")

if __name__ == "__main__":
    main()
