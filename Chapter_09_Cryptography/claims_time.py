from datetime import datetime, timedelta, timezone
from time import sleep, time
import jwt
import warnings
warnings.filterwarnings("ignore")

iat = datetime.now(tz=timezone.utc)
nfb = iat + timedelta(seconds=1)
exp = iat + timedelta(seconds=3)
data = {"payload": "data", "nbf": nfb, "exp": exp, "iat": iat}

def decode(token, secret):
    print(time())
    try:
        print(jwt.decode(token, secret, algorithms=["HS256"]))
    except (
            jwt.ImmatureSignatureError, jwt.ExpiredSignatureError
    ) as err:
        print(err)
        print(type(err))

def main():
    secret = "secret-key"
    token = jwt.encode(data, secret)

    for _ in range(4):
        decode(token, secret)
        sleep(2)

if __name__ == "__main__":
    main()