from datetime import datetime
import logging
import os
import sys
import time


def main():
    print ("DUDA, your personalized learning tool")

    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('this is an error')

        
if __name__ == '__main__':
    main()
