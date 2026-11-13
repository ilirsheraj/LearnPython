import secrets

def get_reset_pwd_url(token_length=16):
    token = secrets.token_urlsafe(token_length)
    return f"https://example.com/reset-pwd/{token}"

def main():
    print(get_reset_pwd_url())
    print()
    print(get_reset_pwd_url(token_length=32))

if __name__ == "__main__":
    main()