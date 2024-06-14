def analyze_response(response):
    if any(header in response.headers for header in ['Injected-Header', 'Test-Header', 'X-Injected-Header']):
        return True
    return False
