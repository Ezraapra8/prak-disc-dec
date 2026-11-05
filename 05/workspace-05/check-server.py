import sys
import requests

def check_server(host, port):
    url = f"http://{host}:{port}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            print("Server up")
        else:
            print("Server down")
    except Exception:
        print("Server down")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    port = sys.argv[2] if len(sys.argv) > 2 else "44777"
    check_server(host, port)