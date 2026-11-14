import jwt
import warnings
warnings.filterwarnings("ignore")

data = {"payload": "data", "iss": "hein", "aud": "learn-python"}
secret = "secret-key"
token = jwt.encode(data, secret)

def decode(token, secret, issuer=None, audience=None):

    try:
        print(jwt.decode(token, secret, issuer=issuer,
                         audience=audience, algorithms=["HS256"]))
    except (
            jwt.InvalidIssuerError, jwt.InvalidAudienceError,
    ) as err:
        print(err)
        print(type(err))

decode(token, secret)