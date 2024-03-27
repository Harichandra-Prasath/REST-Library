import jwt


def encode_jwt(payload):
    encoded_jwt = jwt.encode(payload,"SECRET",algorithm="HS256")
    return encoded_jwt

def decode_jwt(token):
    decoded_payload = jwt.decode(token,"SECRET",algorithms="HS256")
    return decoded_payload