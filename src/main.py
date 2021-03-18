import logging
import os
import sys

from utils import *



def main():
    print ("DataBook")

    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('this is an error')



    q = Quantity(name="aubergines", unity=None)

#     Involtini aux aubergines
# 2 aubergines 
# 1 boule de moza
# 30 g de parmesan
# 30cl de sauce tomate
# sel, origan

#     Salade italienne
# 250g tomate cerise
# 5g pignon de pin
# 1/2 boule de moza
# basilic
# 10g parmesan
# 2cs huile olive


        
if __name__ == '__main__':
    main()
