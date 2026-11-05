import requests
import pybreaker

breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)

@breaker
def make_http_request(url):
    print(f"Attempting to access {url}...")
    response = requests.get(url, timeout=2)
    response.raise_for_status()
    print(f"Successfully accessed {url}")
    return response.text

if __name__ == "__main__":
    try:
        make_http_request("http://localhost:44777")
    except Exception as e:
        print(f"Circuit Breaker Catch: {e}")