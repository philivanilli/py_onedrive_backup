# -*- coding: UTF-8 -*-

import logging

__log_instance = None
__log_handle_instance = None


def setup(**kwargs):
    """
    Setups an application wide loggign instance.
    """
    global __log_instance
    global __log_handle_instance

    # create logger
    __log_instance = logging.getLogger('application')
    __log_instance.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s %(levelname)9s: %(message)s')

    # create console handler and set level to debug
    if 'logtofile' in kwargs and kwargs['logtofile'] is True:
        __log_handle_instance = logging.FileHandler('onedrive_backup.log')
    else:
        __log_handle_instance = logging.StreamHandler()
    __log_handle_instance.setLevel(logging.DEBUG)

    # add formatter to console handler
    __log_handle_instance.setFormatter(formatter)

    # register log handlers
    __log_instance.addHandler(__log_handle_instance)


def critical(msg, *args, **kwargs):
    """
    Log a message with severity 'CRITICAL' on the application logger.
    The application logger should be configured by calling setup() before.
    """
    if __log_instance:
        __log_instance.critical(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the application logger.
    The application logger should be configured by calling setup() before.
    """
    if __log_instance:
        __log_instance.error(msg, *args, **kwargs)


def exception(msg, *args, exc_info=True, **kwargs):
    """
    Log a message with severity 'ERROR' on the application logger, with exception
    information. The application logger should be configured by calling setup() before.
    """
    error(msg, *args, exc_info=exc_info, **kwargs)


def warning(msg, *args, **kwargs):
    """
    Log a message with severity 'WARNING' on the application logger.
    The application logger should be configured by calling setup() before.
    """
    if __log_instance:
        __log_instance.warning(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """
    Log a message with severity 'INFO' on the application logger.
    The application logger should be configured by calling setup() before.
    """
    if __log_instance:
        __log_instance.info(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    """
    Log a message with severity 'DEBUG' on the application logger.
    The application logger should be configured by calling setup() before.
    """
    if __log_instance:
        __log_instance.debug(msg, *args, **kwargs)


def log(level, msg, *args, **kwargs):
    """
    Log 'msg % args' with the integer severity 'level' on the application logger.
    The application logger should be configured by calling setup() before.
    """
    if __log_instance:
        __log_instance.log(level, msg, *args, **kwargs)
