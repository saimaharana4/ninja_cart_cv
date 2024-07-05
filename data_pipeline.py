# from data_preprocessing.data_gathering import *
# from data_preprocessing.cleanup_script import *
# import os
# from dotenv import load_dotenv


# def main():
#     # Load environment variables from .env file
#     load_dotenv()

#     google_drive_url = os.getenv("google_drive_url")
#     downloaded_file = os.getenv("downloaded_file")
#     extract_to = os.getenv("extract_to")

#     google_drive_url = google_drive_url
#     downloaded_file = downloaded_file
#     extract_to = extract_to

#     # Download the file
#     download_file_from_google_drive(google_drive_url, downloaded_file)

#     # Verify the file is a valid zip
#     if not zipfile.is_zipfile(downloaded_file):
#         print(f"Error: '{downloaded_file}' is not a valid ZIP file. Please check the URL and try again.")
#         return

#     # Extract the file
#     extract_zip(downloaded_file, extract_to)

#     # cleanup script, remove the zip file 
#     remove_file(downloaded_file)

# if __name__ == '__main__':
#     main()


from data_preprocessing.data_gathering import *
from data_preprocessing.cleanup_script import *
from data_preprocessing.data_transformers import DownloadFileTransformer, ExtractZipTransformer, RemoveFileTransformer
from data_preprocessing.data_gathering import *
from data_preprocessing.cleanup_script import *
from dotenv import load_dotenv
from sklearn.pipeline import Pipeline
import os
import logging
from log.logger_config import setup_logger

# Setup logging
logger = setup_logger("log\logging.log")

def main():
    # Load environment variables from .env file
    load_dotenv()

    google_drive_url = os.getenv("google_drive_url")
    downloaded_file = os.getenv("downloaded_file")
    extract_to = os.getenv("extract_to")

    # Define the pipeline
    pipeline = Pipeline([
        ('download', DownloadFileTransformer(url=google_drive_url, output_path=downloaded_file)),
        ('extract', ExtractZipTransformer(zip_path=downloaded_file, extract_to=extract_to)),
        ('cleanup', RemoveFileTransformer(file_path=downloaded_file))
    ])

    # Execute the pipeline
    try:
        pipeline.fit_transform([None])  # Pass a dummy value to fit_transform
        logger.info("Data Gathering Pipeline executed successfully.")
    except ValueError as e:
        logger.error(e)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
