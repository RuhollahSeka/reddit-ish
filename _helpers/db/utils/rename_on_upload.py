import os
import uuid


class RenameOnUpload:
    def __init__(self, directory):
        self.directory = directory

    def __call__(self, instance, filename):
        _, extension = os.path.splitext(filename)
        file_uuid = uuid.uuid4()
        new_filename = f'{self.directory}{file_uuid}{extension}'
        return new_filename
