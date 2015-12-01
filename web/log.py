#!/usr/bin/env python3

import logging
import logging.handlers
import os.path as path

def configure_logger(logger_name='root',
                     log_dir='/tmp/',
                     filename='',
                     disable_stdout=False,
                     disable_file=False):
    """
    Returns logger which output to stdout and and to specified file.
    Example: log = configure_logger(filename='abc.log')
    will output log with timestamps to /tmp/abc.log
    """

    if not filename:
        filename = logger_name + '.log'
    log_location = path.join(log_dir, filename)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.handlers = []

    log_format = u'[%(asctime)s]  %(message)s'
    formatter = logging.Formatter(log_format)

    # Stdout
    if not disable_stdout:
        stdout = logging.StreamHandler()
        stdout.setLevel(logging.INFO)
        stdout.setFormatter(formatter)
        logger.addHandler(stdout)

    # Filehandler
    if not disable_file:
        file_handler = logging.handlers.RotatingFileHandler(
            log_location, mode='a', maxBytes=10**7, backupCount=1)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger