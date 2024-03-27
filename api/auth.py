from typing import Any
from rest_framework.authentication import BaseAuthentication
from .utils import decode_jwt
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from .exceptions import noTokenException,invalidTokenException,invalidRoleException

class roleAuthentication(BaseAuthentication):
    def __init__(self,role) -> None:
        self.role = role
    
    def __call__(self) -> Any:
        return self

    def authenticate(self, request):
        
        jwt_token = request.COOKIES.get("jwt","")
        if jwt_token=="":
            raise noTokenException(token="JWT")
         
        payload = decode_jwt(jwt_token)

        id = payload["ID"]

        try: 
            _user = User.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise invalidTokenException()

        return (_user,None)