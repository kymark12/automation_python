import logging


def test_loggingd_demo():
    # Logger object
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('logfile.log')
    """
    log format: 
    %(asctime)s - Adds timestamps on the log
    %(levelname)s - Adds the specific level of logging of the event
    %(name)s - Adds the name of the test file where the failure occurred
    %(message)s - Adds the message of log level
    """
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)  # file handler object

    logger.setLevel(logging.DEBUG)

    # List of the levels of logging
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happened")
    logger.critical("Critical issue")
