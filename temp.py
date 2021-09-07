import  jwt
encoded_jwt = jwt.encode({"Name": "Hardik"}, "secret", algorithm="HS256")
print(encoded_jwt)
decoded = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
print(decoded)
