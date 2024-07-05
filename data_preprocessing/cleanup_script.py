import os
import logging
from pathlib import Path

from log.logger_config import setup_logger

# Setup logging
logger = setup_logger('log\logging.log')

def remove_file(file_path):
    """
    Remove the specified file and log the process.
    
    :param file_path: Path to the file to be removed
    """
    file_path = Path(file_path)
    
    if file_path.exists():
        try:
            os.remove(file_path)
            logger.info(f"Successfully deleted the file: {file_path}")
        except Exception as e:
            logger.error(f"Failed to delete the file: {file_path}. Error: {e}")
    else:
        logger.warning(f"File not found: {file_path}")