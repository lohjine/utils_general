
import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, log_file, level=logging.DEBUG, stream = False):
    """
    To setup as many loggers as you want

    USAGE:
    # first file logger
    logger = setup_logger('first_logger', 'first_logfile.log')
    logger.info('This is just info message')

    # second file logger
    super_logger = setup_logger('second_logger', 'second_logfile.log')
    super_logger.error('This is an error message')

    REFERENCE:
    https://stackoverflow.com/questions/11232230/logging-to-two-files-with-different-settings
    """

    handler = logging.FileHandler(log_file, 'w+') # https://stackoverflow.com/a/52039216
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    if stream:
        logger.addHandler(logging.StreamHandler())

    return logger


import linecache
import sys


def PrintException(logger = None):
    """
    Prints real exception:
        "EXCEPTION IN (<ipython-input-1414-7f2a340f6b82>, LINE 15 "print(1/0)"): division by zero"
    """

    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)

    error_str = f'EXCEPTION IN ({filename}, LINE {lineno} "{line.strip()}"): {exc_obj}'

    if logger:
        logger.error(error_str)
    else:
        print(error_str)
