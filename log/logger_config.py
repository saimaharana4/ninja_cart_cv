import logging

def setup_logger(log_file):
    """
    Sets up the logger to log messages to both a file and the console.
    
    :param log_file: The file path for the log file
    """
    logger = logging.getLogger('ninjacart_logger')
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Adding handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

