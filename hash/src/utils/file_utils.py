import os

class FileUtils:
    @staticmethod
    def is_file(path):
        return os.path.isfile(path)
    
    @staticmethod
    def get_file_size(file_path):
        return os.path.getsize(file_path)
    
    @staticmethod
    def read_file_chunks(file_path, chunk_size=8192):
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk