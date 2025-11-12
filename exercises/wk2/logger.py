# logger.py
import logging
from config import LOG_FILE

def setup_logger(name):
    LOG_FILE.parent.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # File handler
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.INFO)
    
    # Console handler (optional)
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger

# main.py
from logger import setup_logger

logger = setup_logger(__name__)
logger.info("Application started")
