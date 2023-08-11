#!/usr/bin/env python3
import logging
import pprint

# Configure the logger
logging.basicConfig(filename='log.txt',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Create a logger instance
logger = logging.getLogger()

# Use like this
#logger.info('This is a log entry.' + '\n')

