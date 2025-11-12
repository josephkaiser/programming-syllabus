import logging
# import mylib
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    # mylib.do_somthing()
    logger.info('Finished')



