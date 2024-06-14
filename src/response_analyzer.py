def analyze_response(response):
    # Check for custom injected headers
    if any(header in response.headers for header in ['Injected-Header', 'Test-Header', 'X-Injected-Header']):
        return True
    # Additional checks for CRLF indicators in the response body or headers
    if 'Injected-Header: CRLF' in response.text or 'Test-Header: Test' in response.text:
        return True
    return False
