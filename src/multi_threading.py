import threading

class MultiThreadScanner:
    def __init__(self, scanner, urls, num_threads=10):
        self.scanner = scanner
        self.urls = urls
        self.num_threads = num_threads
        self.results = []

    def worker(self, urls):
        for url in urls:
            print(f"Scanning URL: {url}")  # Debugging output
            self.results.extend(self.scanner.check_crlf_injection(url))

    def run(self):
        threads = []
        chunk_size = len(self.urls) // self.num_threads
        for i in range(self.num_threads):
            chunk = self.urls[i * chunk_size:(i + 1) * chunk_size]
            thread = threading.Thread(target=self.worker, args=(chunk,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return self.results
