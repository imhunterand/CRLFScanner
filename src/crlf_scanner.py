import requests
from urllib.parse import urlparse
from .response_analyzer import analyze_response

class CRLFScanner:
    def __init__(self, payloads):
        self.payloads = payloads

    def check_crlf_injection(self, url):
        results = []
        for payload in self.payloads:
            try:
                parsed_url = urlparse(url)
                target_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{parsed_url.query}{payload}"
                print(f"Testing URL: {target_url}")  # Debugging output

                response = requests.get(target_url)
                print(f"Response Headers: {response.headers}")  # Debugging output

                if analyze_response(response):
                    results.append((url, payload, "Vulnerable"))
                else:
                    results.append((url, payload, "Not Vulnerable"))
            except Exception as e:
                results.append((url, payload, f"Error: {e}"))
        return results
