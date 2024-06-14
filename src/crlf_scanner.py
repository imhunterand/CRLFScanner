import requests
from urllib.parse import urlparse

class CRLFScanner:
    def __init__(self, payloads):
        self.payloads = payloads

    def check_crlf_injection(self, url):
        results = []
        for payload in self.payloads:
            try:
                parsed_url = urlparse(url)
                target_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{parsed_url.query}{payload}"
                
                response = requests.get(target_url)
                
                # Check for CRLF Injection indication in response headers
                if any(header in response.headers for header in ['Injected-Header', 'Test-Header', 'X-Injected-Header']):
                    results.append((url, payload, "Vulnerable"))
                else:
                    results.append((url, payload, "Not Vulnerable"))
            except Exception as e:
                results.append((url, payload, f"Error: {e}"))
        return results
