from config import ConfigFile
from jose import jwt

class AccessToken:
    def createToken(username: str):
        token_data = {"sub": username}
        return jwt.encode(token_data, ConfigFile.SECRET_KEY, algorithm=ConfigFile.ALGORITHM)