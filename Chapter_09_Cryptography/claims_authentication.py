import jwt
import warnings
warnings.filterwarnings("ignore")

# data = {"payload": "data", "iss": "hein", "aud": "learn-python"}
# secret = "secret-key"
# token = jwt.encode(data, secret)

def decode(token, secret, issuer=None, audience=None):

    try:
        print(jwt.decode(token, secret, issuer=issuer,
                         audience=audience, algorithms=["HS256"]))
    except (
            jwt.InvalidIssuerError, jwt.InvalidAudienceError,
    ) as err:
        print(err)
        print(type(err))

def main():
    data = {"payload": "data", "iss": "hein", "aud": "learn-python"}
    secret = "secret-key"
    token = jwt.encode(data, secret)
    decode(token, secret)
    print()
    # No issuer
    decode(token, secret, audience="learn-python")
    print()
    # No audience
    decode(token, secret, issuer="hein")
    print()
    # Both break
    decode(token, secret, issuer="wrong", audience="learn-python")
    print()
    decode(token, secret, issuer="hein", audience="wrong")
    print()
    decode(token, secret, issuer="hein", audience="learn-python")

if __name__ == "__main__":
    main()