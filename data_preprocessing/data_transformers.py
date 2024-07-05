from sklearn.base import BaseEstimator, TransformerMixin
from data_preprocessing.data_gathering import download_file_from_google_drive, extract_zip
from data_preprocessing.cleanup_script import remove_file
import zipfile
import logging

class DownloadFileTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path

    def fit(self, X=None, y=None):
        return self

    def transform(self, X=None):
        download_file_from_google_drive(self.url, self.output_path)
        return self

class ExtractZipTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, zip_path, extract_to):
        self.zip_path = zip_path
        self.extract_to = extract_to

    def fit(self, X=None, y=None):
        return self

    def transform(self, X=None):
        if not zipfile.is_zipfile(self.zip_path):
            raise ValueError(f"Error: '{self.zip_path}' is not a valid ZIP file.")
        extract_zip(self.zip_path, self.extract_to)
        return self

class RemoveFileTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, file_path):
        self.file_path = file_path

    def fit(self, X=None, y=None):
        return self

    def transform(self, X=None):
        remove_file(self.file_path)
        return self
