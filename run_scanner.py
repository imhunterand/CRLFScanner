import argparse
from src.url_loader import load_urls
from src.crlf_scanner import CRLFScanner
from src.multi_threading import MultiThreadScanner
from src.logger import Logger

def main():
    parser = argparse.ArgumentParser(description='CRLF Injection Scanner')
    parser.add_argument('-u', '--urls', type=str, required=True, help='File path of URLs')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file path for results')
    parser.add_argument('-p', '--payloads', type=str, default='payloads/payloads.txt', help='File path of payloads')
    parser.add_argument('-t, '--threads', type=int, default=10, help='Number of threads')

    args = parser.parse_args()

    print(f"Loading URLs from {args.urls}")  # Debugging output
    urls = load_urls(args.urls)
    print(f"Loaded URLs: {urls}")  # Debugging output

    print(f"Loading payloads from {args.payloads}")  # Debugging output
    payloads = load_urls(args.payloads)
    print(f"Loaded payloads: {payloads}")  # Debugging output

    scanner = CRLFScanner(payloads)
    multi_thread_scanner = MultiThreadScanner(scanner, urls, args.threads)

    results = multi_thread_scanner.run()

    logger = Logger(args.output)
    logger.log(results)

    # Print summary of results
    print(f"Results: {results}")  # Debugging output
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
