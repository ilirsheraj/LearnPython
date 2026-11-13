import hmac
import hashlib

def calc_digest(key, message):
    key = bytes(key, 'utf-8')
    message = bytes(message, 'utf-8')
    dig = hmac.new(key, message, hashlib.sha512)
    return dig.hexdigest()

def main():
    mac = calc_digest("secret-key", "Important Message")
    print(mac)

if __name__ == '__main__':
    main()