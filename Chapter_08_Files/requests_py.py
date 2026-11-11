import requests
# for better printing
import json

urls = {
    "get": "https://httpbin.org/get?t=learn+python+programming",
    "headers": "https://httpbin.org/headers",
    "ip": "https://httpbin.org/ip",
    "user-agent": "https://httpbin.org/user-agent",
    "UUID": "https://httpbin.org/uuid",
    "JSON": "https://httpbin.org/json",
}

def get_contents(title, url):
    resp = requests.get(url)
    print(f"Response for {title}")
    # print(resp.json())
    print(json.dumps(resp.json(), indent=4))

def main():
    for title, url in urls.items():
        get_contents(title, url)
        print("-" * 40)

if __name__ == "__main__":
    main()