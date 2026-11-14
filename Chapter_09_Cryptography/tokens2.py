import jwt
import warnings
warnings.filterwarnings("ignore")

data = {"payload": "data", "id": 123456789}

token512 = jwt.encode(data, "secret-key", algorithm="HS512")
data_out = jwt.decode(token512, "secret-key", algorithms=["HS512"])
print(data_out)