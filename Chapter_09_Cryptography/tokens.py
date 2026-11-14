import jwt
import warnings
warnings.filterwarnings("ignore")

data = {"payload": "data", "id": 123456789}

token = jwt.encode(data, "secret-key")
algs = ["HS256", "HS512"]

data_out = jwt.decode(token,"secret-key",algorithms=algs)
print(token)
print()
print(data_out)
print()
data_out2 = jwt.decode(token, options={"verify_signature": False})
print(data_out2)