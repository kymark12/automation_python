import inspect
import logging


class BaseClass:

    @staticmethod
    def get_logger():
        logger_name = inspect.stack()[1][3]
        # Logger object
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # file handler object

        logger.setLevel(logging.DEBUG)
        return logger
