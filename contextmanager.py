# These are object that are used to manage resources and perfom setup and cleanup action 
# for specific context. 
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Usage:
with FileManager("example.txt", "r") as file:
    contents = file.read()
    print("Contents of the file:")
    print(contents)
