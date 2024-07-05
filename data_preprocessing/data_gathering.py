import zipfile
from pathlib import Path
import gdown
import os

from log.logger_config import setup_logger

# Setup logging
logger = setup_logger("log\logging.log")

def download_file_from_google_drive(url, output_path):
    output_path = Path(output_path)
    output_dir = output_path.parent
    
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
    
    gdown.download(url, str(output_path), quiet=False, fuzzy=True)
    logger.info(f"Downloaded file to {output_path}")
    print(f"Downloaded file to {output_path}")

def extract_zip(zip_path, extract_to):
    zip_path = Path(zip_path)
    extract_to = Path(extract_to)
    
    if not extract_to.exists():
        extract_to.mkdir(parents=True, exist_ok=True)
        
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        logger.info(f"Extraction complete. Files are extracted to '{extract_to}'")
        print(f"Extraction complete. Files are extracted to '{extract_to}'")
    except zipfile.BadZipFile:
        logger.error(f"Error: '{zip_path}' is not a valid ZIP file")
        print(f"Error: '{zip_path}' is not a valid ZIP file")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")


