class File:
    def __init__(self, filename: str):
        self.filename = filename
    
    def read(self) -> str:
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 'Файл не найден'

            