import csv

class Logger:
    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, results):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Payload", "Result"])
            for result in results:
                writer.writerow(result)
